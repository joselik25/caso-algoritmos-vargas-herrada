# C6 – Selección del algoritmo de ordenamiento

## Caso analizado

El caso corresponde al control de inventario de rollos de tela de una tienda de tapices. El inventario se administra mediante Excel y cada rollo cuenta con un identificador único.

## Algoritmo seleccionado

Se selecciona Quick Sort como algoritmo de ordenamiento para organizar los registros del inventario por su identificador (ID_Rollo).

## Justificación

La selección se fundamenta en las mediciones realizadas durante la práctica C5. Quick Sort obtuvo los menores tiempos de ejecución en los cuatro tamaños evaluados:

- 500 registros: 0.00188417 segundos.
- 1.000 registros: 0.00433743 segundos.
- 2.000 registros: 0.00887790 segundos.
- 4.000 registros: 0.01781727 segundos.

En comparación, Merge Sort presentó tiempos ligeramente mayores y Bubble Sort fue considerablemente más lento.

Quick Sort tiene un rendimiento promedio de O(n log n), por lo que resulta adecuado para ordenar conjuntos de registros de tamaño considerable.

## Consideraciones

La elección se limita a la operación de ordenamiento. Para las búsquedas y actualizaciones frecuentes del inventario será necesario evaluar otras estructuras de datos, considerando que los rollos se identifican individualmente y que sus existencias cambian con cada corte o merma.

## Conclusión

De acuerdo con los resultados obtenidos, Quick Sort es la alternativa seleccionada para ordenar los registros del inventario, debido a que presentó el mejor rendimiento en las pruebas realizadas. Esta decisión se apoya en las mediciones experimentales y en su complejidad temporal promedio.