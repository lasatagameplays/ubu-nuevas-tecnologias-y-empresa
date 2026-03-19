# Proyecto Gephi – Análisis de la red email-Eu-core

En este proyecto se ha realizado el análisis de la red **email-Eu-core** utilizando la herramienta **Gephi**.

La red representa las comunicaciones por correo electrónico entre miembros de una institución y se ha modelado como un **grafo dirigido**, donde los nodos representan usuarios y las aristas los envíos de correos.

## Análisis realizado

- Se llevó a cabo una **partición de la red en comunidades** mediante el cálculo de la **modularidad**.
- Se calculó el **grado de los nodos**, utilizado posteriormente para representar su importancia relativa.
- Se calculó el **coeficiente de clustering**, obteniendo un valor medio que indica una tendencia moderada a la formación de agrupaciones locales.
- Se generó una **visualización de la red** utilizando el algoritmo de layout **ForceAtlas2**, donde:
  - El **color de los nodos** representa la comunidad a la que pertenecen.
  - El **tamaño de los nodos** es proporcional a su grado.

## Entregables

- Archivo del proyecto de Gephi: `email-Eu-core.gephi`
- Imagen de la red resultante: `email-Eu-core.png`

