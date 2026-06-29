# 🏆 Informe Técnico Kaggle: Link Prediction - LosTrifuerza

## Arquitectura de Victoria Consolidada (Score: 0.53486)

El equipo **LosTrifuerza** ha estabilizado su posición mediante una arquitectura de promediado múltiple diseñada para anular la varianza aleatoria y maximizar la precisión estructural.

### 1. Ingeniería de Atributos (42 Features)
Mantenemos el núcleo de 42 variables topológicas que extraen la esencia de la red universitaria (Jaccard, Adamic-Adar, Caminos de longitud 2 y 3, y Matrices de Katz). Se ha validado que este enfoque es superior a los embeddings ruidosos en redes de este tamaño.

### 2. Multi-Seed Averaging (Estrategia Grandmaster)
La principal mejora de esta versión es el uso de **Seed Averaging**. En lugar de realizar un único entrenamiento, ejecutamos el proceso completo 5 veces utilizando 5 semillas aleatorias distintas (42, 123, 777, 2026, 999). 
Esto afecta directamente a la selección del 50% de los ejemplos negativos (*Hard Negative Mining*), permitiendo que el modelo vea diferentes configuraciones de "trampas" y aprenda una frontera de decisión mucho más robusta.

### 3. Ensemble de 15 Modelos
El resultado final es el promedio de **15 modelos** de Gradient Boosting (5 iteraciones de XGBoost + LightGBM + CatBoost). Al promediar las probabilidades, reducimos el error de generalización y estabilizamos la posición en el Leaderboard.

### 4. Umbralización Top-1200
Se mantiene el criterio de selección rígido de los **1200 enlaces más probables**, un umbral validado empíricamente como el punto óptimo para maximizar el F1-Score en este dataset.

---

## 📂 Lo que hay en los archivos
- **`Proyecto_LosTrifuerza.ipynb`**: Notebook principal con la ejecución del Multi-Seed Averaging.
- **`main_LosTrifuerza.py`**: Script de producción sincronizado con la lógica del Notebook.
- **`submission_LosTrifuerza.csv`**: Archivo de resultados con Score 0.53486.
- **`requirements.txt`**: Dependencias actualizadas.