#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LosTrifuerza - Predicción de Enlaces

===================================================

File name: main_LosTrifuerza.py

===================================================

Description: The Ultimate Triforce (Sincronizado con Jupyter Score 0.53170). 
Implementación de Multi-Seed Averaging (5 semillas) sobre la arquitectura 
de la Fiera Deidad (XGB + LGB + CB) para máxima estabilidad y precisión.

===================================================

Authors:
    - Roberto Iturralde Zarzo
    - Ruben Castaneda Matute

===================================================
    
Asignatura: Nuevas Tecnologias y Empresa (UBU)
Profesor: Jose Ignacio Santos Martin
"""

import warnings
warnings.filterwarnings('ignore')

import scipy.linalg
import numpy as np
scipy.linalg.triu = np.triu  # Parche de compatibilidad

import networkx as nx
import pandas as pd
import math
import time
import os

from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from community import community_louvain

# ============================================================
# CONFIGURACIÓN DEL PROYECTO
# ============================================================
GRAFO_FILE = './ArchivosKaggle/social_network_training.gexf'
TEST_FILE = './ArchivosKaggle/test.csv'
OUTPUT_FILE = 'submission_LosTrifuerza.csv'

SEED_BASE = 42
SEEDS = [42, 123, 777, 2026, 999] # Las 5 semillas del éxito
NEG_RATIO = 2.0          
N_PREDICTED_TRUE = 1200  

def compute_graph_features(G):
    print("Calculando comunidades (Louvain)...")
    partition = community_louvain.best_partition(G, random_state=SEED_BASE)
    
    print("Calculando métricas de nodo y centralidades...")
    deg = dict(G.degree())
    deg_cent = nx.degree_centrality(G)
    pagerank = nx.pagerank(G, alpha=0.85)
    clustering = nx.clustering(G)
    core = nx.core_number(G)
    
    try:
        eigen = nx.eigenvector_centrality_numpy(G)
    except Exception:
        eigen = {n: 0.0 for n in G.nodes()}
        
    closeness = nx.closeness_centrality(G)
    
    try:
        betw = nx.betweenness_centrality(G, k=min(200, G.number_of_nodes()), seed=SEED_BASE)
    except Exception:
        betw = {n: 0.0 for n in G.nodes()}
        
    avg_nbr_deg = nx.average_neighbor_degree(G)
    neighbors = {n: set(G.neighbors(n)) for n in G.nodes()}
    
    return {
        'partition': partition, 'deg': deg, 'deg_cent': deg_cent, 'pagerank': pagerank,
        'clustering': clustering, 'core': core, 'eigen': eigen, 'closeness': closeness,
        'betw': betw, 'avg_nbr_deg': avg_nbr_deg, 'neighbors': neighbors,
    }

def katz_matrix(G, beta=0.005):
    nodes = list(G.nodes())
    idx = {v: i for i, v in enumerate(nodes)}
    A = nx.to_numpy_array(G, nodelist=nodes, dtype=float)
    try:
        K = np.linalg.inv(np.eye(len(nodes)) - beta * A) - np.eye(len(nodes))
    except Exception:
        return None, None
    return K, idx

def precompute_path_matrices(G):
    nodes = list(G.nodes())
    idx = {v: i for i, v in enumerate(nodes)}
    A = nx.to_numpy_array(G, nodelist=nodes, dtype=np.float32)
    A2 = A @ A
    np.fill_diagonal(A2, 0)
    A3 = A2 @ A
    np.fill_diagonal(A3, 0)
    return A2, A3, idx

def extract_features(G, pairs, gf, katz, katz_idx, A2, A3, A_idx):
    partition = gf['partition']; deg = gf['deg']; deg_cent = gf['deg_cent']
    pagerank = gf['pagerank']; clustering = gf['clustering']; core = gf['core']
    eigen = gf['eigen']; closeness = gf['closeness']; betw = gf['betw']
    avg_nbr_deg = gf['avg_nbr_deg']; neighbors = gf['neighbors']

    total_size = 42
    rows = np.zeros((len(pairs), total_size), dtype=np.float32)

    for i, (u, v) in enumerate(pairs):
        if u not in neighbors or v not in neighbors:
            continue

        Nu = neighbors[u]; Nv = neighbors[v]
        cn = Nu & Nv; un = Nu | Nv
        cn_c = len(cn); un_c = len(un) if un else 1

        jaccard = cn_c / un_c if un else 0.0
        aa = 0.0; ra = 0.0
        for w in cn:
            d = deg[w]
            if d > 1:
                aa += 1.0 / math.log(d); ra += 1.0 / d
        pref = deg[u] * deg[v]
        lhn = cn_c / pref if pref > 0 else 0.0
        salton = cn_c / math.sqrt(pref) if pref > 0 else 0.0
        sorensen = 2 * cn_c / (deg[u] + deg[v]) if (deg[u] + deg[v]) > 0 else 0.0
        hub_prom = cn_c / min(deg[u], deg[v]) if min(deg[u], deg[v]) > 0 else 0.0
        hub_dep = cn_c / max(deg[u], deg[v]) if max(deg[u], deg[v]) > 0 else 0.0

        same_comm = 1 if partition.get(u) == partition.get(v) else 0
        cn_sh = sum(1 for w in cn if partition.get(w) == partition.get(u) == partition.get(v))
        ra_sh = sum(1.0/deg[w] for w in cn if deg[w] > 0 and partition.get(w) == partition.get(u) == partition.get(v))

        u_dc, v_dc = deg_cent[u], deg_cent[v]
        u_pr, v_pr = pagerank[u], pagerank[v]
        u_cl, v_cl = clustering[u], clustering[v]
        u_cr, v_cr = core[u], core[v]
        u_eg, v_eg = eigen.get(u, 0.0), eigen.get(v, 0.0)
        u_cs, v_cs = closeness[u], closeness[v]
        u_bt, v_bt = betw[u], betw[v]
        u_an, v_an = avg_nbr_deg.get(u, 0.0), avg_nbr_deg.get(v, 0.0)

        deg_diff = abs(deg[u] - deg[v]); deg_sum = deg[u] + deg[v]
        deg_min = min(deg[u], deg[v]); deg_max = max(deg[u], deg[v])
        log_deg_sum = math.log(1 + deg[u]) + math.log(1 + deg[v])

        fof_u = set()
        for w in Nu: fof_u |= neighbors[w]
        fof_u -= Nu; fof_u.discard(u)
        fof_v = set()
        for w in Nv: fof_v |= neighbors[w]
        fof_v -= Nv; fof_v.discard(v)
        fof_common = len(fof_u & fof_v)
        v_in_fof_u = 1 if v in fof_u else 0

        katz_uv = 0.0
        if katz is not None and u in katz_idx and v in katz_idx:
            katz_uv = float(katz[katz_idx[u], katz_idx[v]])

        rows[i, 0:37] = [
            jaccard, aa, ra, pref, lhn, salton, sorensen, hub_prom, hub_dep, cn_c,
            same_comm, cn_sh, ra_sh, u_dc, v_dc, u_pr, v_pr, u_cl, v_cl, u_cr, v_cr, 
            u_eg, v_eg, u_cs, v_cs, u_bt, v_bt, u_an, v_an, deg_diff, deg_sum, 
            deg_min, deg_max, log_deg_sum, fof_common, v_in_fof_u, katz_uv,
        ]

        if u in A_idx and v in A_idx:
            iu, iv = A_idx[u], A_idx[v]
            rows[i, 37] = float(A2[iu, iv])  
            rows[i, 38] = float(A3[iu, iv])  
            
        rows[i, 39] = 2 if cn_c > 0 else (3 if v in fof_u else 5)
        rows[i, 40] = sum(1.0 / (math.log(deg[w]+1) ** 2 + 0.1) for w in cn if deg[w] > 1)
        rows[i, 41] = sum(1.0 / math.sqrt(deg[w]) for w in cn if deg[w] > 0)

    return rows

def generate_advanced_negatives(G, n_needed, seed):
    rng = np.random.default_rng(seed)
    existing = set()
    for u, v in G.edges(): existing.add((u, v)); existing.add((v, u))
    nodes = list(G.nodes()); seen = set(); negs = []
    
    hard_candidates = []
    for u in nodes:
        for w in G.neighbors(u):
            for v in G.neighbors(w):
                if u != v and v not in G.neighbors(u): hard_candidates.append(tuple(sorted([u, v])))
    
    hard_candidates = list(set(hard_candidates)); rng.shuffle(hard_candidates)
    n_hard = min(int(n_needed * 0.5), len(hard_candidates)) 
    for i in range(n_hard):
        negs.append(hard_candidates[i]); seen.add(hard_candidates[i])
        
    while len(negs) < n_needed:
        u, v = rng.choice(nodes, 2, replace=False)
        key = tuple(sorted([u, v]))
        if key not in existing and key not in seen:
            seen.add(key); negs.append(key)
    return negs

def main():
    print("\n" + "="*60)
    print("  LosTrifuerza — Link Prediction — UBU 2025-2026")
    print("  Rubén Castañeda Matute & Roberto Iturralde Zarzo")
    print("="*60)
    print("\n  ⏱   El programa puede tardar varios minutos en terminar la ejecución.")
    print("  ☕  Tómate un café o un colacado tranquilamente.")
    print("\n" + "="*60)
    print("\n")

    if not os.path.exists(GRAFO_FILE) or not os.path.exists(TEST_FILE):
        print("ERROR: Faltan archivos de datos.")
        return
    
    t_total = time.time()


    print("\n" + "="*60)
    print("")
    print("Cargando grafo...")
    t = time.time()
    G = nx.read_gexf(GRAFO_FILE)
    G = nx.relabel_nodes(G, {n: str(n) for n in G.nodes()})

    gf = compute_graph_features(G)
    katz, katz_idx = katz_matrix(G, beta=0.005)
    A2, A3, A_idx = precompute_path_matrices(G)

    pos_edges = list(G.edges())
    n_neg = int(len(pos_edges) * NEG_RATIO)
    spw = n_neg / len(pos_edges)
    print(f"    ({time.time()-t:.1f}s)", flush=True)
    print("\n" + "="*60)
    print("")

    print("Extrayendo variables de enlaces reales...")
    t = time.time()
    X_pos = extract_features(G, pos_edges, gf, katz, katz_idx, A2, A3, A_idx)
    print(f"    ({time.time()-t:.1f}s)", flush=True)
    print("\n" + "="*60)
    print("")

    print("Procesando archivo de Test...")
    t = time.time()
    test_df = pd.read_csv(TEST_FILE)
    test_pairs = [tuple(str(x).split('-')) for x in test_df['Id']]
    X_test = extract_features(G, test_pairs, gf, katz, katz_idx, A2, A3, A_idx)

    all_probs = []
    print(f"    ({time.time()-t:.1f}s)", flush=True)
    print("\n" + "="*60)
    print("")
    # --- BUCLE DE SEED AVERAGING ---
    for current_seed in SEEDS:
        print(f"\n--- 🛡️ ENTRENANDO TRIFUERZA CON SEMILLA {current_seed} ---")
        t = time.time()
        neg_edges = generate_advanced_negatives(G, n_neg, seed=current_seed)
        X_neg = extract_features(G, neg_edges, gf, katz, katz_idx, A2, A3, A_idx)

        X_train = np.vstack([X_pos, X_neg])
        y_train = np.array([1] * len(X_pos) + [0] * len(X_neg))

        lgb = LGBMClassifier(n_estimators=800, num_leaves=63, learning_rate=0.03, subsample=0.85, 
                             colsample_bytree=0.85, scale_pos_weight=spw, random_state=current_seed, verbose=-1)
        lgb.fit(X_train, y_train)

        xgb = XGBClassifier(n_estimators=800, max_depth=6, learning_rate=0.03, subsample=0.85, 
                            colsample_bytree=0.85, scale_pos_weight=spw, random_state=current_seed, 
                            eval_metric='logloss', tree_method='hist')
        xgb.fit(X_train, y_train)

        cb = CatBoostClassifier(iterations=800, depth=6, learning_rate=0.03, auto_class_weights='Balanced', 
                                random_seed=current_seed, verbose=0)
        cb.fit(X_train, y_train)
        
        p_lgb = lgb.predict_proba(X_test)[:, 1]
        p_xgb = xgb.predict_proba(X_test)[:, 1]
        p_cb = cb.predict_proba(X_test)[:, 1]
        all_probs.append((p_lgb + p_xgb + p_cb) / 3.0)

        print(f"    ({time.time()-t:.1f}s)", flush=True)
        print("\n" + "="*60)
        print("")

    print("\nPromediando Inteligencia de las 5 Semillas...")
    final_probs = np.mean(all_probs, axis=0)
    top_idx = np.argsort(-final_probs)[:N_PREDICTED_TRUE]
    final_preds = np.zeros(len(final_probs), dtype=bool)
    final_preds[top_idx] = True

    test_df['Predicted'] = final_preds
    test_df.to_csv(OUTPUT_FILE, index=False)

    print("")
    print()
    print("\n" + "="*60)
    print("")
    print(f"[OK] Archivo generado: {OUTPUT_FILE}")
    print(f"     True predichos:   {final_preds.sum()} / {len(final_preds)}")
    print(f"     Tiempo total:     {time.time()-t_total:.1f}s")
    print("\n" + "="*60)

if __name__ == '__main__':
    main()