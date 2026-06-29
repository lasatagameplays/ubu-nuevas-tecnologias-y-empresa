# Práctica Análisis de la Vulnerabilidad en Redes


## Objetivo

El objetivo de esta práctica es analizar la vulnerabilidad y robustez de redes complejas, centrándose en el comportamiento de una red de Barabási-Albert ante errores aleatorios y ataques dirigidos. Además, se comparan estos resultados con los de una red aleatoria de Erdős-Rényi, utilizando simulaciones de Montecarlo para evaluar la conectividad tras fallos sucesivos.


## Método

Vamos a evaluar la robustez de una red en términos de conectividad, medida como la fracción de nodos que permanecen en el componente mayor. La idea es someter a una red a "modificaciones" en forma de desconexión de nodos de la red y ver cómo cambia la conectividad. Proponemos el siguiente procedimiento (similar al trabajo original de Barabasi):

1. Generación de una red aleatoria (de Erdös-Rényi o de Barabási-Albert)
2. Simulación de errores aleatorios y ataques dirigidos para desconectar nodos de la red
3. Replicación de los experimentos varias veces debido al carácter aleatorio del modelo
4. Visualización de los resultados mediante gráficas que muestran la conectividad promedio tras cada paso de desconexión

## Actividades

Se pide completar un notebook de Jupyter con el análisis que describimos a continuación.

### 1. Robustez a errores aleatorios en una red Barabasi-Álbert

#### 1.1 Experimento de simulación

- Replicar el siguiente experimento un número de veces $T$ (por ejemplo 10):
  1. Generar una red de Barabási-Albert con $m_0=3$, $m=3$ y $N=1000$ nodos
  2. Eliminar secuencialmente los enlaces de un nodo seleccionado al azar (no seleccionado antes)
  3. Tras cada desconexión, calcular la conectividad de la red como la fracción de nodos que permanecen en el componente mayor

#### 1.2 Visualización de resultados

- Representar gráficamente la evolución temporal de la conectividad promedio (para las diferentes replicaciones):
  - Eje $x$: número de nodos desconectados
  - Eje $y$: conectividad promedio tras cada desconexión

### 2. Robustez a ataques dirigidos en una red Barabasi-Álbert

#### 2.1 Experimento de simulación

- Replicar el siguiente experimento un número de veces $T$:
  1. Generar una red de Barabási-Albert con $m_0=3$, $m=3$ y $N=1000$ nodos
  2. Eliminar secuencialmente los enlaces del nodo con mayor grado
  3. Tras cada desconexión, calcular la conectividad de la red como la fracción de nodos que permanecen en el componente mayor

#### 2.2 Visualización de resultados

- Representar gráficamente la evolución temporal de la conectividad promedio (para las diferentes replicaciones):
  - Eje $x$: número de nodos eliminados
  - Eje $y$: conectividad promedio tras cada desconexión

### 3 Análisis de los resultados

- Indicar si la red es más resistente a errores aleatorios o ataques dirigidos. Proporcionar una breve explicación de la diferencia observada.

### 4 Análisis de Erdős-Rényi

Repite el ejercicio de simulación de errores aleatorios y ataques dirigidos utilizando un modelo de red aleatoria de Erdős-Rényi. Analiza los resultados, compáralos con los de la red de Barabasi-Albert y extrae conclusiones.

## Entregable

Sube al repositorio el archivo del notebook Jupyter (.ipynb), asegurándote de que todas las celdas de código estén ejecutadas y los resultados visibles. Incluye explicaciones breves en texto donde sea necesario.

## Evaluación y temporalización 

La evaluación manual del notebook tendrá en cuenta la precisión del código, su organización, claridad en la documentación, calidad de las visualizaciones y la capacidad para justificar e interpretar los resultados. La fecha límite será la indicada en la tarea de Moodle, y los envíos retrasados estarán sujetos a una penalización del 30% de la nota total.

## Referencias
- R. Albert, H. Jeong, and A.-L. Barabási, "Error and attack tolerance of complex networks" *Nature*, vol. 406, pp. 378–382, 2000. [link](https://www-nature-com.ubu-es.idm.oclc.org/articles/35019019)

