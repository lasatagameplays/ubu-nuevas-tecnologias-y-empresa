"""
File name: assignment.py
Description: function to compute the modularity of a graph and to detect communities by Girvan-Newman algorithm

Authors:
    - Ruben Castañeda Matute
    - Roberto Iturralde Zarzo
    
License:
    This script is licensed under the MIT License. 
    https://opensource.org/licenses/MIT
"""

import networkx as nx
import numpy as np
import pandas as pd


# Function to compute the modularity of a graph
def modularity(G, partition):
    """
    Funcion para calcular la modularidad Q de una partición en un grafo G.
    
    Usamos la fórmula:    Q = (1 / 2m) * sum_{i,j} [ A_ij - (k_i * k_j) / (2m) ] * delta(c_i, c_j)
    
    donde:
        - A_ij  = 1 si existe enlace entre i y j, 0 si no
        - k_i   = grado del nodo i
        - m     = número total de enlaces en el grafo
        - delta = 1 si i y j están en la misma comunidad, 0 si no
    """

    # Número total de enlaces en el grafo
    m = G.number_of_edges()

    # Aqui obtenemos la matriz de adyacencia como array de numpy
    # nodelist fija el orden de los nodos para que coincida con los índices
    nodes = list(G.nodes())
    A = nx.to_numpy_array(G, nodelist=nodes, weight=None)

    # Vector de grados: k[i] = grado del nodo i
    degrees = dict(G.degree())
    k = np.array([degrees[n] for n in nodes])

    # Aqui construimos un diccionario que mapea cada nodo a su comunidad (índice de comunidad)
    # Así podemos saber rápidamente si dos nodos están en la misma comunidad
    node_to_community = {}
    for community_index, community in enumerate(partition):
        for node in community:
            node_to_community[node] = community_index

    # Aqui calculamos la suma doble de la fórmula de modularidad
    Q = 0.0
    for i, node_i in enumerate(nodes):
        for j, node_j in enumerate(nodes):
            # delta = 1 solo si ambos nodos están en la misma comunidad
            if node_to_community[node_i] == node_to_community[node_j]:
                # Contribución del par (i, j): [A_ij - k_i*k_j / (2m)]
                Q += A[i, j] - (k[i] * k[j]) / (2 * m)

    # Aqui dividimos por 2m para completar la fórmula
    Q = Q / (2 * m)

    return Q


# Function to detect communities by Girvan-Newman algorithm
def girvan_newman_communities(G):
    """
    Ahora implementamos el algoritmo de Girvan-Newman para detección de comunidades.
    
    El algoritmo funciona así:
        1. Calcular la betweenness (centralidad) de todos los enlaces
        2. Eliminar el enlace con mayor betweenness
        3. Si al eliminar ese enlace la red se divide (split), calcular la
           modularidad de esa partición respecto al grafo original y guardarla
        4. Repetir hasta que no queden enlaces
    
    Devuelve:
        - best_partition : lista de conjuntos de nodos con la mejor partición encontrada
        - best_modularity : valor de modularidad de esa partición
        - modularity_evolution : lista con todos los valores de modularidad calculados
                                  en cada split (en orden cronológico del algoritmo)
    """

    # Trabajamos sobre una copia para no modificar el grafo original
    H = G.copy()

    # Aqui guardamos el número de componentes conexas inicial
    # (normalmente 1, es decir, el grafo está completamente conectado)
    previous_components = nx.number_connected_components(H)

    # Estas son listas para almacenar la evolución de la modularidad
    modularity_evolution = []

    # Estas son variables para guardar la mejor partición encontrada
    best_partition = None
    best_modularity = -np.inf

    # Repetimos mientras queden enlaces en el grafo
    while H.number_of_edges() > 0:

        # Aqui el paso 1: calcular la betweenness de todos los enlaces actuales
        # edge_betweenness_centrality devuelve un dict {(u,v): valor}
        edge_betweenness = nx.edge_betweenness_centrality(H)

        # Aqui el paso 2: identificar el enlace con mayor betweenness y eliminarlo
        # max() con key nos da la clave (par de nodos) con el valor más alto
        edge_to_remove = max(edge_betweenness, key=edge_betweenness.get)
        H.remove_edge(*edge_to_remove)

        # Aqui el paso 3: comprobar si al eliminar ese enlace se ha producido un "split"
        # (es decir, si la red se ha dividido en más componentes que antes)
        current_components = nx.number_connected_components(H)

        if current_components > previous_components:
            # Se ha producido un split: calculamos la modularidad de esta partición
            # Las comunidades son los componentes conexos del grafo actual
            # pero evaluados sobre el grafo ORIGINAL G
            partition = list(nx.connected_components(H))

            # Aqui calculamos la modularidad respecto al grafo original
            Q = modularity(G, partition)

            # Ahora guardamos este valor en la lista de evolución
            modularity_evolution.append(Q)

            # Si esta modularidad es la mejor hasta ahora, la guardamos
            # Usamos >= en lugar de > para cubrir casos de empate exacto
            # y garantizar que best_modularity == np.max(evo) siempre
            if Q >= best_modularity:
                best_modularity = Q
                best_partition = partition

            # Ahora actualizamos el número de componentes previo
            previous_components = current_components

    return best_partition, best_modularity, modularity_evolution
