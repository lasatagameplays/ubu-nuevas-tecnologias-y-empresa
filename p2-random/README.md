# Práctica Red Aleatoria
## Objetivo  
El objetivo principal de esta práctica es implementar una función propia que genere una red aleatoria no dirigida, un modelo común en el análisis de redes que se estudiará con más detalle en el tema de modelos de redes aleatorios. La función deberá recibir como argumentos:  
- **N**: número de nodos  
- **P**: probabilidad de que el par de nodos  (i, j) tenga un enlace  

Y devolver como salida:  
- Un objeto `Graph` con la red correspondiente.  

El algoritmo para construir la red es el siguiente:  
1. Crear una red no dirigida con \(N\) nodos.  
2. Para cada par posible de nodos  (i, j), generar un número aleatorio entre [0,1].  
3. Si el número es menor que \(P\), añadir un enlace entre (i, j).  
4. No se permiten enlaces múltiples.  

Este algoritmo es estocástico, por lo que cada ejecución generará una red diferente en términos de enlaces y estructura.  

## Instrucciones

1. Implementa la función según el algoritmo descrito en el script de python `assignment.py` con el nombre `random_network`
2. Completa el notebook con los siguientes experimentos:
3. Genera una red aleatroria con **N=100** y **P=0.01**:  
   - Muestra gráficamente la matriz de adyacencia (ver `matshow` en la ayuda de Matplotlib).  
   - Calcula el número de enlaces y compara este valor con el valor esperado calculado como:  
     $E[l] = P * \binom{N}{2} $  
   - Calcula el grado medio de la red.  
   - Visualiza la red utilizando un layout circular.  
4. Genera una red aleatroria con **N=100** y **P=0.05**:  
   - Calcula el número de enlaces y compara este valor con el valor esperado.  
   - Calcula el grado medio de la red.  
   - Calcula el camino más corto entre dos pares de nodos **U** y **V** (variables libremente escogidas).  
   - Visualiza la red y el camino más corto calculado anteriormente. 
5. Genera una red aleatroria con **N=1000** y **P=0.005**:  
   - Calcula el número de enlaces y compara este valor con el valor esperado.  
   - Visualiza la red. 

## Entregable

Completa el script de Python y el notebook del repositorio (con celdas ejecutadas y mostrando resultados gráficos).  

## Evaluación y temporalización 

Al realizar un `push` al repositorio, se ejecutarán tests automáticos de evaluación que aportarán una puntuación de 50 sobre 100. Los 50 puntos restantes corresponderán a la evaluación manual del notebook, considerando la precisión del código, su organización, claridad en la documentación, calidad de las visualizaciones y la capacidad para justificar e interpretar los resultados. La fecha límite será la indicada en la tarea de Moodle, y los envíos retrasados estarán sujetos a una penalización del 30% de la nota total.
