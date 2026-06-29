"""
File name: assignment.py
Description: function to compute the centrlity ranking of the nodes of a graph

Authors:
    - Rubén Castañeda Matute
    - Roberto Iturralde Zarzo 
    
License:
    This script is licensed under the MIT License. 
    https://opensource.org/licenses/MIT
"""

import networkx as nx
import numpy as np
import pandas as pd




# Function to compute the centrlity ranking of the nodes of a graph
def net_ranking(G,weights):
    #Esta función calcula una clasificación de centralidad combinada para los nodos en un grafo.

    pagerank_weight, betweenness_weight = weights
    
    # Aquí calculamos las centralidades
    pagerank_dict = nx.pagerank(G)
    betweenness_dict = nx.betweenness_centrality(G)
    
    # Aquí construimos el DataFrame
    df = pd.DataFrame({
        'node_id': list(G.nodes()),
        'pagerank': list(pagerank_dict.values()),
        'betweenness': list(betweenness_dict.values())
    })
    
    # Aquí normalizamos las métricas al rango [0, 1] (Min-Max Scaling)
    pr_min, pr_max = df['pagerank'].min(), df['pagerank'].max()
    bw_min, bw_max = df['betweenness'].min(), df['betweenness'].max()
    
    # Aquí manejamos las divisiones por cero en caso de que los grafos sean completamente uniformes
    pr_norm = (df['pagerank'] - pr_min) / (pr_max - pr_min) if pr_max > pr_min else 0
    bw_norm = (df['betweenness'] - bw_min) / (bw_max - bw_min) if bw_max > bw_min else 0
    
    # Aquí calculamos el índice combinado (average_index)
    df['average_index'] = (pagerank_weight * pr_norm) + (betweenness_weight * bw_norm)
    
    # Aquí ordenamos de mayor a menor según average_index
    df = df.sort_values(by='average_index', ascending=False).reset_index(drop=True)
    
    return df

