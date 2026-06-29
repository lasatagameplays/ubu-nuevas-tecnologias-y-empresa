"""
assignment.py

Pequeño script para calcular el número esperado de relaciones inmunizadas
en una red cuando se aplica una estrategia de vacunación.

Cada nodo = persona
Cada arista = relación/contacto

Si vacunamos a una persona, se "protegen" todas sus relaciones directas.
Por tanto, el número de relaciones inmunizadas es simplemente el grado del nodo.

Autor: Roberto Iturralde Zarzo, Rubén Castañeda Matute.
"""
# Aquí hacemos la importación de las librerias necesarias para este programa
import networkx as nx
import numpy as np


def random_vaccine(G):
    """
    Estrategia de vacunación aleatoria.

    Idea:
    elegimos una persona al azar y la vacunamos.

    El número de relaciones protegidas será el número de vecinos
    que tiene esa persona (su grado).

    El valor esperado de esta estrategia es simplemente
    el grado medio de la red.
    """

    # Aquí guardamos todos los grados de los nodos
    grados = []

    for nodo in G.nodes():
        # Aquí degree(nodo) nos dice cuántos vecinos tiene
        grados.append(G.degree(nodo))

    # Aquí calculamos la media de todos los grados
    # esto equivale al valor esperado de relaciones inmunizadas
    esperado = np.mean(grados)

    # Aquí devolvemos el resultado esperado
    return esperado



def indirect_random_vaccine(G):
    """
    Estrategia de vacunación aleatoria indirecta (Cálculo Teórico Exacto).

    Funcionamiento:
    1) elegimos una persona al azar (probabilidad 1/N)
    2) elegimos uno de sus vecinos (probabilidad 1/grado_nodo_inicial)
    3) vacunamos a ese vecino
    """
    # Aquí hacemos la importación de las librerias necesarias para esta función
    import numpy as np
    
    # Aquí definimos los parametros necesarios para el programa
    esperado = 0
    N = G.number_of_nodes()
    
    # Aquí recorremos cada nodo como si fuera el paso 1 (Elegir al azar)
    for nodo in G.nodes():
        vecinos = list(G.neighbors(nodo))
        
        if len(vecinos) > 0:
            # Aquí obtenemos los grados de todos sus vecinos
            grados_vecinos = [G.degree(v) for v in vecinos]
            
            # Vemos que el valor esperado que aporta este nodo es la media de los 
            # grados de sus vecinos, multiplicado por 1/N (probabilidad de empezar en él)
            esperado += np.mean(grados_vecinos) / N

    # Aquí devolvemos el resultado esperado
    return esperado