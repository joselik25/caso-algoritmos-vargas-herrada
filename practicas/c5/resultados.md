# C5 – Torneo de algoritmos de ordenamiento

## Objetivo

Comparar el rendimiento de Bubble Sort, Merge Sort y Quick Sort mediante pruebas con diferentes cantidades de datos sintéticos.

## Procedimiento

Se utilizaron conjuntos de 500, 1.000, 2.000 y 4.000 números generados aleatoriamente. Para cada algoritmo se realizó un calentamiento y tres mediciones, calculando el promedio de los tiempos obtenidos.

Se comprobó que los tres algoritmos produjeran los mismos resultados ordenados.

## Resultados

| Registros | Bubble Sort (s) | Merge Sort (s) | Quick Sort (s) |
|---:|---:|---:|---:|
| 500 | 0.04148820 | 0.00329827 | 0.00188417 |
| 1.000 | 0.15246477 | 0.00578717 | 0.00433743 |
| 2.000 | 0.73462807 | 0.01196547 | 0.00887790 |
| 4.000 | 3.05290187 | 0.02259390 | 0.01781727 |

## Análisis

Bubble Sort presentó los mayores tiempos de ejecución y su rendimiento empeoró considerablemente al aumentar la cantidad de elementos.

Merge Sort y Quick Sort mostraron tiempos mucho menores. Quick Sort obtuvo el menor tiempo en las cuatro pruebas realizadas.

## Conclusión

Según las mediciones, Quick Sort fue el algoritmo más rápido en los conjuntos evaluados, seguido de Merge Sort. Bubble Sort presentó el peor rendimiento, especialmente con 4.000 elementos.

Los resultados coinciden con el comportamiento esperado de sus complejidades: Bubble Sort tiene un costo promedio de O(n²), mientras que Merge Sort y Quick Sort presentan un rendimiento promedio de O(n log n).

Las mediciones pueden variar por las condiciones del equipo y el ruido del entorno de ejecución. Los resultados corresponden a datos sintéticos y no a registros privados de la tienda.