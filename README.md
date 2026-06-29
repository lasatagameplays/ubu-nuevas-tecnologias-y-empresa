# 🌐 Prácticas de Nuevas Tecnologías y Empresa - UBU

En este repositorio se encuentra el conjunto completo de proyectos y resoluciones correspondientes a la asignatura **Nuevas Tecnologías y Empresa** (4º Curso del Grado en Ingeniería Informática) de la Universidad de Burgos (UBU), curso 2025-2026.

👥 **Autores:**
* **Rubén Castañeda Matute** - ([@lasatagameplays](https://github.com/lasatagameplays))
* **Roberto Iturralde Zarzo** - ([@itujunior](https://github.com/itujunior))

---

## 📊 Información y Calificaciones
* **Notas de la asignatura:** [Descargar Notas_Asignatura.xlsx](./Notas_Asignatura.xlsx)
* **Criterios de evaluación:** [GuiaDocente-NuevasTecnologíasYEmpresa-Curso-2025-2026](./GuiaDocente-NuevasTecnologíasYEmpresa-Curso-2025-2026.pdf)

---

## 📂 Contenido del Repositorio
La estructura del proyecto está diseñada para albergar todo el ciclo de la asignatura de forma organizada:

* 📁 **PRACTICAS/**: Contiene las subcarpetas dedicadas a cada una de las entregas.
  * `p1-gephi/`
  * `p2-random/`
  * `p3-vaccine/`
  * `p4-centrality/`
  * `p5-modularity/`
  * `p6-powerlaw/`
  * `p7-vulnearbility/`
  * `ProyectoFinal/`
* 📄 **Notas_Asignatura.xlsx**: Registro detallado de las calificaciones obtenidas.
* 📄 **GuiaDocente-NuevasTecnologíasYEmpresa-Curso-2025-2026.pdf**: Documentación oficial sobre los criterios de valoración.

---

## 📑 Índice del Curso
La asignatura se compone de un total de 8 proyectos (7 regulares y 1 competitivo), estructurados de la siguiente forma:

### 📘 Prácticas Regulares
1. **Práctica 1:** Análisis Visual con Gephi (email-Eu-core)
2. **Práctica 2:** Red Aleatoria (Random Network)
3. **Práctica 3:** Estrategias de vacunación
4. **Práctica 4:** Medidas de centralidad
5. **Práctica 5:** Cálculo de la modularidad y algoritmo de Girvan-Newman
6. **Práctica 6:** Distribuciones Power Law
7. **Práctica 7:** Análisis de vulnerabilidad de redes

### 👑 Proyectos Finales y Extra
* 🏆 **Proyecto Final (Kaggle):** Link Prediction (Primer Puesto Absoluto)

---

## ⚙️ Requisitos para la Ejecución

**Para las prácticas de Python:**
* Tener **Anaconda Navigator** descargado e instalado.
* Tener **Jupyter Notebook 7.2.2** (o superior).
* Tener Python instalado nativamente y Visual Studio 2022.
* Al abrir el Jupyter, seleccionar el kernel y ejecutar en Python 3.12.4.

**Para la práctica de Análisis Visual:**
* Descargar e instalar **Gephi** desde su [página oficial](https://gephi.org/).
* Es requisito indispensable tener **Java** instalado en el equipo para poder abrir el proyecto.

## 💻 Entorno de Pruebas (Mi Setup)
Aquí dejo mi equipo, en el cual funcionan al 100% los programas y entornos:

* **Lenguaje:** Python 3 (ipykernel) / Java (para Gephi)
* **Entorno Conda:** versión 24.7.1
* **Sistema Operativo:** Windows 11 Pro 64-bit
* **Hardware:** Intel i7-11800H | 16GB RAM | RTX 3050 Ti

---

## 🌌 Práctica 1: Análisis Visual con Gephi (email-Eu-core)

El objetivo de esta primera práctica es el análisis de la red **email-Eu-core** utilizando la herramienta de visualización de grafos **Gephi**.

La red representa las comunicaciones por correo electrónico entre miembros de una institución y se ha modelado como un **grafo dirigido**, donde los nodos representan usuarios y las aristas los envíos de correos. En el estudio se ha llevado a cabo una partición en comunidades mediante el cálculo de la modularidad, análisis del coeficiente de clustering, y una renderización gráfica estructurada con el algoritmo *ForceAtlas2*.

### 🏆 Resultados Académicos
* **Calificación obtenida:** 80.00 / 100.00
* **Evaluador:** José Ignacio Santos Martín
* **Comentario del profesor:** "Bien aunque también se pedía calcular el grado. Echo en falta una mínima descricpción de la red que se analiza, qué representa y la fuente de donde se ha obtenido el dataset."
* **Autores:** Rubén Castañeda Matute y Roberto Iturralde Zarzo.

### 🚀 Instrucciones de Ejecución
Para visualizar y explorar el análisis de la red, sigue estos pasos:
1. Asegúrate de tener **Gephi** instalado en tu equipo (requiere entorno Java).
2. Abre el archivo del proyecto ubicado en: `PRACTICAS/p1-gephi/email-Eu-core.gephi`.
3. En el espacio de trabajo de Gephi, podrás explorar la red donde el **color de los nodos** representa la comunidad a la que pertenecen y el **tamaño** es proporcional a su grado de interacción.

---

## 🕸️ Práctica 2: Red Aleatoria (Random Network)

El objetivo de esta segunda práctica es implementar una función propia en Python que genere una **red aleatoria no dirigida**, un modelo estocástico básico en el análisis de redes complejas. 

El algoritmo recibe como parámetros el número de nodos ($N$) y la probabilidad de enlace ($P$), evaluando las combinaciones posibles para construir la red sin permitir enlaces múltiples ni autoenlaces. Posteriormente, el proyecto realiza una serie de tres experimentos escalonados (desde $N=100$ hasta $N=1000$) utilizando `NetworkX` y `Matplotlib` para analizar:
* La representación gráfica de la **matriz de adyacencia**.
* La comparativa entre el número de enlaces reales y el valor esperado matemáticamente ($E[l] = P * \binom{N}{2}$).
* El cálculo del grado medio de la red.
* La extracción y renderizado visual del **camino más corto** (shortest path) entre dos nodos seleccionados.

### 🏆 Resultados Académicos
* **Calificación obtenida:** 100.00 / 100.00
* **Evaluador:** José Ignacio Santos Martín
* **Comentario del profesor:** "Correcto"
* **Autores:** Rubén Castañeda Matute y Roberto Iturralde Zarzo.

### 🚀 Instrucciones de Ejecución
Para reproducir los experimentos y la generación de la red:
1. Asegúrate de tener instalado Python 3 y las dependencias correspondientes (`networkx`, `numpy`).
2. Abre y ejecuta todas las celdas del Jupyter Notebook ubicado en `PRACTICAS/p2-random/random_network.ipynb` para visualizar las gráficas de los nodos, la matriz de adyacencia y la validación de las métricas.

---

## 💉 Práctica 3: Estrategias de vacunación

El objetivo de esta tercera práctica es evaluar y comparar la eficacia de distintas estrategias de inmunización (vacunación) para detener la propagación de epidemias en una red compleja, utilizando Python y `NetworkX`.

El proyecto implementa y simula dos enfoques para distribuir un presupuesto limitado de $V$ vacunas:
1. **Estrategia Aleatoria (Random Strategy):** Selección uniforme de $V$ nodos al azar.
2. **Estrategia Aleatoria Indirecta (Indirect Random Strategy):** Selección de $V$ nodos al azar para, a continuación, vacunar a un vecino (amigo) seleccionado aleatoriamente de cada uno.

El análisis demuestra de forma práctica y empírica la **Paradoja de la Amistad** (*Friendship Paradox*). A través de la simulación de brotes infecciosos y curvas de propagación con `Matplotlib`, se confirma matemáticamente que la estrategia indirecta es drásticamente más efectiva, ya que aumenta drásticamente las probabilidades de localizar y neutralizar a los súper-propagadores (nodos hub con un alto grado de conexiones).

### 🏆 Resultados Académicos
* **Calificación obtenida:** 100.00 / 100.00
* **Evaluador:** José Ignacio Santos Martín
* **Comentario del profesor:** "Muy bien"
* **Autores:** Rubén Castañeda Matute y Roberto Iturralde Zarzo.

### 🚀 Instrucciones de Ejecución
Para reproducir la simulación de la epidemia y las estrategias de vacunación:
1. Asegúrate de tener instaladas las dependencias.
2. Abre y ejecuta las celdas del Jupyter Notebook en `PRACTICAS/p3-vaccine/vaccine_strategy.ipynb`. Este generará la red base y dibujará las gráficas comparativas de rendimiento (porcentaje de nodos infectados vs. número de vacunas).

---

## 📊 Práctica 4: Medidas de centralidad

El objetivo de esta cuarta práctica es identificar y aplicar las métricas de centralidad más adecuadas para analizar y explicar la importancia relativa (el poder o influencia) de los nodos en diferentes redes complejas.

El proyecto implementa un motor de clasificación en Python utilizando `NetworkX` y `Pandas` que calcula un índice combinado (*Average Index*) mediante la normalización (Min-Max Scaling) y la ponderación de dos métricas clave: **PageRank** y **Betweenness Centrality**. 

Este sistema de clasificación se aplica a dos casos de estudio reales:
1. **Red de Fútbol (Mundial 1998):** Análisis de una red dirigida que representa las conexiones y transferencias internacionales de los jugadores (`football98.net`).
2. **Familias Florentinas del Renacimiento:** Análisis de alianzas matrimoniales (dataset de Breiger y Pattison). El código demuestra matemáticamente por qué la familia **Medici** alcanzó el poder hegemónico frente a rivales como los Pazzi: se posicionaron como el principal *hub* de la red, obteniendo el valor más alto de *Betweenness Centrality* para controlar el flujo de relaciones.

### 🏆 Resultados Académicos
* **Calificación obtenida:** 85.00 / 100.00
* **Evaluador:** José Ignacio Santos Martín
* **Comentario del profesor:** "Bastante bien. Un comentario en las métricas utilizadas. La estructura dirigida de la red de fútbol hace posible emplear HITS, una métrica que distingue entre authorities y hubs y aporta información relevante sobre las ligas más fuertes y las canteras con mayor capacidad de generación de talento."
* **Autores:** Rubén Castañeda Matute y Roberto Iturralde Zarzo.

### 🚀 Instrucciones de Ejecución
Para visualizar el análisis de centralidad:
1. Asegúrate de tener instaladas las dependencias (`networkx`, `numpy`, `pandas`, `scipy`, `matplotlib`).
2. Abre y ejecuta el Jupyter Notebook en `PRACTICAS/p4-centrality/centrality_analysis.ipynb`. Este cargará los datasets de su respectiva carpeta, generará los rankings combinados y renderizará visualmente los grafos.

---

## 🧩 Práctica 5: Cálculo de la modularidad y algoritmo de Girvan-Newman

El objetivo de esta quinta práctica es comprender y aplicar la detección de comunidades en redes complejas, evitando depender de funciones predefinidas (cajas negras) y programando desde cero las métricas clave.

El proyecto implementa en Python dos algoritmos fundamentales:
1. **Cálculo de la Modularidad ($Q$):** Una función matemática propia para evaluar la calidad de una partición en comunidades, comparando la densidad de enlaces internos frente a lo que se esperaría en una red generada al azar.
2. **Algoritmo de Girvan-Newman:** Implementación iterativa que detecta comunidades eliminando progresivamente los enlaces con mayor *Edge Betweenness Centrality* (poder de intermediación). En cada división, se calcula la modularidad para registrar el punto óptimo de partición.

El modelo se pone a prueba empíricamente con la famosa red del **Club de Karate de Zachary**. Los resultados del Notebook demuestran cómo el algoritmo, sin información previa, logra predecir con altísima precisión la división y fractura social histórica que sufrió este club de artes marciales.

### 🏆 Resultados Académicos
* **Calificación obtenida:** 100.00 / 100.00
* **Evaluador:** José Ignacio Santos Martín
* **Comentario del profesor:** "Muy bien"
* **Autores:** Rubén Castañeda Matute y Roberto Iturralde Zarzo.

### 🚀 Instrucciones de Ejecución
Para visualizar el análisis de comunidades y la modularidad:
1. Asegúrate de tener instaladas las dependencias (`networkx`, `numpy`, `pandas`, `matplotlib`).
2. Abre y ejecuta el Jupyter Notebook en `PRACTICAS/p5-modularity/modularity_community_detection.ipynb`. Este cargará la red de Zachary, ejecutará las particiones, dibujará la curva de evolución de la modularidad e imprimirá un grafo coloreado según la división óptima detectada.

---

## 📈 Práctica 6: Distribuciones Power Law

El objetivo de esta sexta práctica es comprender y analizar las distribuciones *Power Law* (Ley de Potencias) en redes complejas, evaluando empíricamente si la topología de una red real se comporta como una red libre de escala (*scale-free*).

El proyecto analiza el dataset de una red de routers de Internet, utilizando `NetworkX` y herramientas estadísticas en Python para:
1. Calcular la distribución de grado y representarla gráficamente.
2. Realizar estimaciones del exponente $\alpha$ mediante un **histograma con clases logarítmicas** y el ajuste de una recta de regresión lineal.
3. Realizar una estimación alternativa y más precisa utilizando la **distribución acumulada** de grado.

Los resultados del cuaderno confirman matemáticamente que la infraestructura de Internet sigue una ley de potencias (con un valor de $\alpha$ entre 2 y 3). Esto demuestra que su conectividad está dominada por unos pocos nodos altamente conectados (*hubs*), lo que confiere a la red una gran robustez frente a fallos aleatorios, pero la hace altamente vulnerable a ataques dirigidos.

### 🏆 Resultados Académicos
* **Calificación obtenida:** 100.00 / 100.00
* **Evaluador:** José Ignacio Santos Martín
* **Comentario del profesor:** "Muy bien"
* **Autores:** Rubén Castañeda Matute y Roberto Iturralde Zarzo.

### 🚀 Instrucciones de Ejecución
Para reproducir el análisis de la distribución:
1. Asegúrate de tener instaladas las dependencias (`networkx`, `numpy`, `pandas`, `matplotlib`, `scipy`).
2. Abre y ejecuta el Jupyter Notebook en `PRACTICAS/p6-powerlaw/power_law_analysis.ipynb`.

---

## 🛡️ Práctica 7: Análisis de vulnerabilidad de redes

El objetivo de esta séptima práctica es analizar empíricamente la vulnerabilidad y robustez topológica de las redes complejas frente a fallos aleatorios y ataques dirigidos (intencionados a los nodos de mayor grado).

El proyecto utiliza `NetworkX` y simulaciones de **Monte Carlo** para evaluar la caída de la conectividad (midiendo el tamaño del componente conexo mayor) conforme se van aislando nodos. Este experimento se realiza sobre dos modelos matemáticos distintos:
1. **Red de Barabási-Albert (Scale-Free):** Demostrando que es altamente robusta frente a errores aleatorios, pero crítica y vulnerable ante ataques dirigidos que destruyen sus *hubs* centrales.
2. **Red de Erdős-Rényi (Random):** Demostrando un comportamiento mucho más homogéneo y lineal, al tener sus grados distribuidos de manera uniforme sin la presencia de súper-propagadores.

### 🏆 Resultados Académicos
* **Calificación obtenida:** 95.00 / 100.00
* **Evaluador:** José Ignacio Santos Martín
* **Comentario del profesor:** "Correcto. Se podría haber añadido intervalos de confianza en las gráficas para mostrar la significación estadística de los resultados de Monte Carlo."
* **Autores:** Rubén Castañeda Matute y Roberto Iturralde Zarzo.

### 🚀 Instrucciones de Ejecución
Para reproducir las simulaciones de vulnerabilidad:
1. Asegúrate de tener instaladas las dependencias necesarias (`networkx`, `numpy`, `pandas`, `matplotlib`).
2. Abre y ejecuta el Jupyter Notebook en `PRACTICAS/p7-vulnearbility/vulnerability.ipynb`.

---

## 🏆 Proyecto Final (Kaggle): Link Prediction (Primer Puesto)

El objetivo de este proyecto final y competitivo es resolver el problema de *Link Prediction* (Predicción de Enlaces) en una red social universitaria incompleta, identificando los 1000 enlaces ocultos o eliminados artificialmente. La resolución de este problema se planteó como una competición abierta en **Kaggle** contra el resto de alumnos.

Bajo el nombre de equipo **"LosTrifuerza"**, diseñamos una arquitectura avanzada de *Machine Learning* que transformaba la topología del grafo en un problema de clasificación binaria. Las claves técnicas del algoritmo ganador fueron:
1. **Feature Engineering Estratégico (42 variables):** Extracción de métricas de similitud estructural (Jaccard, Adamic-Adar, Resource Allocation, Caminos cortos) descartando *embeddings* ruidosos.
2. **Ensemble Multi-Modelo (La Trifuerza):** Un modelo híbrido combinando las predicciones de probabilidad de **XGBoost, LightGBM y CatBoost**.
3. **Multi-Seed Averaging:** Promediado de las ejecuciones en 5 semillas aleatorias distintas con *Hard Negative Mining* (selección iterativa de ejemplos negativos difíciles) para evitar el sobreajuste y estabilizar la frontera de decisión.

El equipo se proclamó **campeón absoluto de la competición** logrando un *score* aplastante en el Leaderboard privado de Kaggle.

### 🏆 Resultados Académicos y Competición
* **Posición en Kaggle:** 1º Puesto absoluto (Score: 0.87798).
* **Calificación obtenida:** 100.00 / 100.00 (+0.5 puntos extra directos a la nota final de la asignatura por ganar la competición).
* **Evaluador:** José Ignacio Santos Martín.
* **Comentario del profesor:** "Muy bien, solo una sugerencia, probar un modelo más sencillo como una regresión logística que permite ver el peso que obtiene cada métrica, lo que ofrece información muy útil."
* **Autores:** Rubén Castañeda Matute y Roberto Iturralde Zarzo.

### 🚀 Instrucciones de Ejecución
Para reproducir la predicción de enlaces:
1. Dirígete a la carpeta `PRACTICAS/ProyectoFinal/` y asegúrate de instalar las dependencias avanzadas con `pip install -r requirements.txt` (incluye `xgboost`, `lightgbm`, `catboost`, etc.).
2. Abre y ejecuta el Jupyter Notebook `Proyecto_LosTrifuerza.ipynb` o ejecuta por consola el script de producción `main_LosTrifuerza.py`.
3. El algoritmo leerá los datasets correspondientes, extraerá las métricas topológicas, entrenará el *Ensemble* iterativo con las 5 semillas y generará el archivo `submission_LosTrifuerza.csv` con las probabilidades.