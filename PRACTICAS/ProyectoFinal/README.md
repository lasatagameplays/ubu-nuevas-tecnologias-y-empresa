# Proyecto Link Prediction Competition

![Logo](./images/kaggle_50294_logos_header.png)

## **Objetivo**

El objetivo de esta competición es diseñar y desarrollar un algoritmo capaz de **identificar enlaces ocultos (*missing links*)** en una red social universitaria construida a partir de interacciones reales por correo electrónico.

A diferencia de un problema de predicción temporal, aquí se trabaja con una única instantánea incompleta de la red. El reto consiste en **recuperar conexiones reales que han sido eliminadas artificialmente**.

Se busca fomentar la aplicación de técnicas de ciencia de redes y aprendizaje automático, así como una correcta validación experimental.

La competición se desarrolla en Kaggle (donde se evalúan las predicciones), mientras que este repositorio recogerá los desarrollos, código y documentación de cada equipo.

## **Descripción del problema**

* Se parte de una red social real completa.
* Se han eliminado un conjunto de enlaces reales (1000 enlaces).
* La red resultante (training graph) es incompleta.
* El objetivo es identificar qué pares de nodos corresponden a enlaces reales eliminados.

El conjunto de test contiene:

* Enlaces reales eliminados (**positivos**)
* Pares de nodos sin conexión (**negativos**)

El problema consiste en clasificar cada par como:

* `True`: existe enlace en la red original
* `False`: no existe enlace

## **Normas de la competición**

### 1. **Formación de equipos**

* Se podrá participar en equipos de hasta 2 personas.
* Cada equipo deberá registrar una única cuenta en Kaggle.
* Para unirse a la competición se utilizará el enlace publicado en UBUvirtual.

### 2. **Objetivo**

* Diseñar un algoritmo que identifique los **1000 enlaces ocultos**.
* Los detalles del dataset están disponibles en Kaggle.

### 3. **Metodología**

* Se pueden utilizar técnicas de:

  * ciencia de redes
  * aprendizaje automático
  * embeddings de grafos
* El problema puede abordarse como:

  * clasificación binaria
  * o ranking de pares de nodos

Durante la competición:

* Se podrán subir predicciones a Kaggle
* Se obtendrá una puntuación basada en el conjunto público

⚠️ Importante:

* El problema es **altamente desbalanceado**
* El conjunto de test contiene tanto negativos fáciles como difíciles

### 4. **Validación**

Recomendaciones:

* Simular el problema real eliminando enlaces del grafo
* Evitar usar directamente non-edges aleatorios como validación
* Mantener coherencia estructural del grafo

### 5. **Entrega final**

* Cada equipo deberá subir al repositorio:

  * código (scripts o notebooks)
  * descripción del método
  * resultados obtenidos
* Fecha límite: indicada en UBUvirtual (penalización por retraso del 30%)

### 6. **Evaluación del proyecto**

* Peso: 20% de la asignatura

Criterios:

* Funcionamiento correcto
* Diseño y justificación del enfoque
* Validación experimental
* Claridad del código y documentación

### 7. **Bonificación adicional**

* Clasificación final en Kaggle:

  * **1º lugar**: +0.5 puntos
  * **2º lugar**: +0.25 puntos
  * **3º lugar**: +0.1 puntos

### 8. **Participación conjunta**

* Modalidad presencial y online compiten conjuntamente en Kaggle
* Evaluación independiente

### 9. **Prácticas desleales**

* Prohibido compartir soluciones entre equipos
* Cualquier manipulación indebida será penalizada

## **Guía técnica (orientativa)**

El problema se basa en patrones estructurales de la red.

Algunas aproximaciones útiles:

* Common Neighbors
* Jaccard Coefficient
* Adamic-Adar
* Preferential Attachment
* Node embeddings (Node2Vec, DeepWalk)
* Modelos supervisados combinando métricas

También es importante:

* gestionar el desbalanceo
* elegir correctamente el umbral de decisión
* o trabajar directamente en términos de ranking

## **Consejos**

En el repositorio se incluyen dos infografías:

* Predicción de enlaces como problema de Machine Learning
* Validación en link prediction


**¡Buena suerte en la competición!**

---
## 🏆 Solución de Máximo Rendimiento - Equipo LosTrifuerza
Para ver en detalle los experimentos y la arquitectura de **Multi-Seed Averaging** que nos otorgó el **Score de 0.53486**, consulta nuestro [Informe Final Técnico](./INFORME_FINAL.md).