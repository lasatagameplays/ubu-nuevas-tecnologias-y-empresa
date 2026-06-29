# Práctica Análisis de Centralidad de Nodos


## Objetivo
El objetivo principal de esta práctica es identificar y aplicar las medidas de centralidad más adecuadas para analizar y explicar la importancia relativa de los nodos en dos redes sociales. Este análisis permitirá destacar la utilidad de las métricas de centralidad en contextos específicos. Primero se trabajará con las fucniones de Networkx para calcular medidadas de centralidad, y después se estudiarán dos casos.

## Instrucciones

### 1. Ranking de nodos

Implementa en el script de python `assignment.py` una función `net_ranking` que reciba como argumentos:
1. una red de nodos (en formato Networkx) 
2. una tupla de dos pesos `(pagerank_weight, betweenness_weight)`


La función devuelve un `DataFrame` de Pandas con un ranking de nodos basado en sus centralidades tal y como se describe a continuación:
1. `node_id`: identificador de cada nodo en la red
2. `pagerank`: valor de la centralidad de PageRank de cada nodo
3. `betweenness`: valor de la centralidad de betweenness de cada nodo
4. `average_index`: valor calculado de un índice combinado, que será la media ponderada de las medidas normalizadas (entre [0,1]) de las centralidades anteriores

`average_index` = `pagerank_weight` * `pagerank` + `betweenness_weight` * `betweenness`

Cunpliendo que `pagerank_weight` + `betweenness_weight` = 1

El `DataFrame` debe estar ordenado de mayor a menor según el índice combinado, es decir, los nodos más importantes aparecerán primero en el ranking.


### 2. Análisis de casos

En un notebook de Jupyter:

#### 2.1. Red de football
La red `football98.net` representa a los 22 equipos internacionales de fútbol que participaron en el Campeonato Mundial de París 1998. Cada arco dirigido del país A al país B indica que al menos un jugador de la selección del país A juega en un equipo del país B durante el resto del año. El peso del arco corresponde al número de jugadores "exportados".

En el **notebook**:
1. Realiza un análisis de centralidad utilizando aquellas métricas que estimes más adecuadas para este caso (se valorará la elección)
2. Dibuja la red y modifica el tamaño y/o color de los nodos según el ranking establecido.
3. Interpreta los resultados, destacando los países más influyentes en términos de la(s) métrica(s) escogidas.

Nota: el formato de la red es Pajek [.NET](https://gephi.org/users/supported-graph-formats/pajek-net-format/)

#### 2.2. Red de familias florentinas del renacimiento
La red de familias florentinas del renacimiento, generada mediante la función `florentine_families_graph` de NetworkX, representa las conexiones matrimoniales entre las familias prominentes de la Florencia renacentista (Padgett).

En el **notebook**:
1. Realiza un análisis de centralidad utilizando aquellas métricas que describe mejor la posición de poder de los Medici frente a los Pazzi.
2. Dibuja la red y modifica el tamaño y/o color de los nodos según el ranking establecido.
3. Interpreta los resultados, destacando los países más influyentes en términos de la(s) métrica(s) escogidas.

Nota: la red de familias Florentinas corresponde al trabajo Breiger R. and Pattison P. (1986). Cumulated social roles: The duality of persons and their algebras. Social Networks, 8, 215-256.

## Entregable

Sube al repositorio el archivo del notebook Jupyter (.ipynb) y el script `assignment.py`, asegurándote de que todas las celdas de código estén ejecutadas y los resultados visibles. Incluye explicaciones breves en texto donde sea necesario.

## Evaluación y temporalización 

Al realizar un `push` al repositorio, se ejecutarán tests automáticos de evaluación que aportarán una puntuación de 30 sobre 100. Los puntos restantes corresponderán a la evaluación manual del notebook, considerando la precisión del código, su organización, claridad en la documentación, calidad de las visualizaciones y la capacidad para justificar e interpretar los resultados. La fecha límite será la indicada en la tarea de Moodle, y los envíos retrasados estarán sujetos a una penalización del 30% de la nota total.









