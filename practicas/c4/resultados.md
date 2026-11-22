# C4 – Comparación de búsqueda lineal y búsqueda binaria

## Objetivo

Comparar el rendimiento de la búsqueda lineal y la búsqueda binaria al localizar un rollo de tela mediante su identificador único (ID_Rollo).

## Procedimiento

Se utilizaron registros sintéticos basados en la estructura del inventario de la tienda de tapices. Se realizaron pruebas con 500, 1.000, 2.000 y 4.000 registros.

Para cada tamaño se realizó un calentamiento y tres mediciones por algoritmo. Se calculó el promedio de los tiempos obtenidos.

La búsqueda lineal recorrió los registros en su orden original. Para la búsqueda binaria se ordenaron previamente los registros por ID_Rollo. En ambos casos se buscó el último registro del conjunto.

## Resultados

| Registros | Búsqueda lineal (s) | Búsqueda binaria (s) | Relación |
|---:|---:|---:|---:|
| 500 | 0.0000675001 | 0.0000052000 | 12.98 veces |
| 1.000 | 0.0001936331 | 0.0000045000 | 43.03 veces |
| 2.000 | 0.0002822666 | 0.0000076999 | 36.66 veces |
| 4.000 | 0.0006570000 | 0.0000073334 | 89.59 veces |

## Análisis

Los resultados muestran que la búsqueda lineal incrementa su tiempo conforme aumenta la cantidad de registros, debido a que puede necesitar recorrer toda la lista.

La búsqueda binaria presentó tiempos menores en las cuatro pruebas. Esto se relaciona con su complejidad O(log n), siempre que los registros estén ordenados por el campo de búsqueda.

## Conclusión sobre el ordenamiento

En el inventario de la tienda, ordenar los registros puede ser conveniente si se realizan búsquedas frecuentes y se mantiene el orden actualizado. Sin embargo, ordenar toda la información antes de cada consulta puede generar un costo adicional. Por ello, resulta más conveniente mantener los datos ordenados o utilizar un índice de búsqueda.