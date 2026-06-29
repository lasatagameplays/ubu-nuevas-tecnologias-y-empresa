"""
File name: assignment.py
Description: function to generate a random undirected graph

Authors:
    - Full name (riz1001@alu.ubu.es) (rcm1009@alu.ubu.es)
    
License:
    This script is licensed under the MIT License. 
    https://opensource.org/licenses/MIT
"""
# Aquí importamos las librerias necesarias para este programa
import networkx as nx
import numpy as np
import random
import itertools

# Function: generate a random undirected graph of n nodes, 
#  being p the probability that two nodes have a link between them

# Función que sirve para  generar un grafo a traves de dos variables que se le pasan por la llama a la Función
# n son el numero de nodos
# p es la probabilidad de que el par de nodos  (i, j) tenga un enlace
def random_network(n, p):
    # Aquí creamos el grafo no dirigido y añadimos los 'n' nodos
    G = nx.Graph()
    G.add_nodes_from(range(n))
    
    # Aquí evaluamos todos los pares posibles (i, j) sin repetición ni autoenlaces
    for i, j in itertools.combinations(range(n), 2):
        # Aquí verificamos que el numero aleatorio generado sea menor que p, para poderlo modificar
        if random.random() < p:
            G.add_edge(i, j)
            
    # Aquí devolvemos el grafo
    return G