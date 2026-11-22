# H2 – Medición de rendimiento

## 1. Objetivo

Comparar el rendimiento de dos métodos para buscar un rollo mediante su identificador único (`ID_Rollo`):

- Búsqueda lineal sobre una lista.
- Búsqueda mediante una tabla hash implementada con un diccionario de Python.

## 2. Procedimiento

Se utilizaron conjuntos de datos sintéticos con los siguientes tamaños:

- 500 registros.
- 1.000 registros.
- 2.000 registros.
- 4.000 registros.

Los datos se generaron tomando como referencia la estructura del archivo `h1/datos.csv` y asignando identificadores únicos.

Para cada tamaño se buscó el último identificador de la colección, de manera que la búsqueda lineal tuviera que recorrer todos los registros.

El protocolo aplicado fue:

1. Generar los datos sintéticos.
2. Preparar la lista y el diccionario con los mismos registros.
3. Ejecutar una búsqueda de calentamiento.
4. Realizar tres mediciones, cada una con 10.000 búsquedas.
5. Calcular el promedio del tiempo por búsqueda.
6. Comparar los resultados y comprobar que ambos métodos encontraran el mismo registro.

Se utilizó `time.perf_counter()` para medir los tiempos de ejecución.

## 3. Resultados obtenidos

| Registros | Búsqueda lineal (s) | Tabla hash (s) | Lineal / Hash | Crecimiento lineal | Crecimiento hash |
|---:|---:|---:|---:|---:|---:|
| 500 | 0.0000836268 | 0.0000002519 | 332.04 | - | - |
| 1.000 | 0.0001108458 | 0.0000001467 | 755.63 | 1.33 | 0.58 |
| 2.000 | 0.0002766716 | 0.0000003513 | 787.53 | 2.50 | 2.39 |
| 4.000 | 0.0006271310 | 0.0000002161 | 2902.17 | 2.27 | 0.62 |

Los tiempos corresponden al promedio por búsqueda, expresado en segundos.

## 4. Análisis de resultados

Los resultados muestran que la búsqueda mediante tabla hash obtuvo tiempos considerablemente menores que la búsqueda lineal en los cuatro tamaños evaluados.

Con 500 registros, la búsqueda lineal tardó 332,04 veces más que la búsqueda con tabla hash. Con 4.000 registros, la diferencia aumentó a 2.902,17 veces.

La búsqueda lineal presentó un incremento del tiempo al aumentar la cantidad de registros, debido a que debe recorrer la lista hasta encontrar el identificador.

La tabla hash mantuvo tiempos muy bajos. Sin embargo, sus valores de crecimiento no fueron constantes, debido a que las mediciones son muy pequeñas y pueden verse afectadas por variaciones del entorno de ejecución.

## 5. Complejidad de las operaciones

- Búsqueda lineal: O(n).
- Búsqueda mediante tabla hash: O(1) promedio.

La diferencia se debe a que la búsqueda lineal examina los registros uno por uno, mientras que el diccionario utiliza el identificador como clave para acceder al registro.

## 6. Conclusión

De acuerdo con las mediciones realizadas, la tabla hash presentó un mejor rendimiento que la búsqueda lineal para localizar rollos mediante su identificador.

Por este motivo, se considera adecuada para las búsquedas frecuentes del inventario, especialmente cuando aumenta la cantidad de registros.

Los resultados corresponden a datos sintéticos y a las condiciones del equipo utilizado. No representan una medición directa del tiempo de trabajo en la tienda.