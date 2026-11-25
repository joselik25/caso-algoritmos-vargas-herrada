JHONMAR VARGAS HERRADA

# I3. Medición del rendimiento

## 1. Procedimiento de medición

Se realizaron pruebas de rendimiento utilizando Python para comparar el algoritmo CompradorIngenuo, basado en fuerza bruta, con CompradorMejorado, basado en programación dinámica.

Para cada tamaño se generaron los mismos datos para ambos algoritmos, utilizando una semilla fija. El presupuesto se calculó como la tercera parte de la suma de los costos de todos los útiles.

El procedimiento de medición consistió en:

- Una ejecución de calentamiento.
- Tres ejecuciones medidas para cada algoritmo.
- Cálculo del promedio de los tres tiempos.
- Comparación de las utilidades obtenidas por ambos algoritmos.

Se utilizó la función `time.perf_counter()` para medir el tiempo de ejecución en segundos.

## 2. Resultados de las mediciones

Se seleccionaron cuatro tamaños: 14, 16, 18 y 20 útiles. El tamaño máximo se mantuvo dentro del intervalo solicitado de 0,5 a 20 segundos para el algoritmo ingenuo.

| Cantidad de útiles | Ingenuo (segundos) | Mejorado (segundos) | Relación de crecimiento |
|---:|---:|---:|---:|
| 14 | 0,052620 | 0,000547 | — |
| 16 | 0,289907 | 0,001368 | 5,51 veces |
| 18 | 1,118847 | 0,001104 | 3,86 veces |
| 20 | 5,133755 | 0,001297 | 4,59 veces |

## 3. Comparación de resultados

En las cuatro mediciones, ambos algoritmos obtuvieron la misma utilidad:

- Con 14 útiles: utilidad de 498.
- Con 16 útiles: utilidad de 548.
- Con 18 útiles: utilidad de 527.
- Con 20 útiles: utilidad de 542.

Los resultados demuestran que ambos algoritmos encuentran la solución óptima para los datos evaluados.

Sin embargo, el algoritmo ingenuo presenta un crecimiento considerable del tiempo de ejecución a medida que aumenta la cantidad de útiles.

El algoritmo mejorado mantiene tiempos mucho menores porque utiliza programación dinámica y evita evaluar todas las combinaciones posibles.

## 4. Relación de crecimiento

Al aumentar la cantidad de útiles de dos en dos, se observaron las siguientes relaciones de crecimiento del algoritmo ingenuo:

- De 14 a 16 útiles: 5,51 veces.
- De 16 a 18 útiles: 3,86 veces.
- De 18 a 20 útiles: 4,59 veces.

Estos resultados son coherentes con el comportamiento exponencial esperado de la fuerza bruta, aunque las mediciones pueden presentar variaciones por las condiciones de ejecución del equipo.

Las diferencias entre las relaciones observadas se deben a que los tiempos reales también pueden verse afectados por otros procesos del sistema y por la variación propia de las mediciones.

## 5. Prueba con 1000 útiles

También se realizó una prueba adicional con 1000 útiles y un presupuesto de 10.000 Bs utilizando el algoritmo mejorado.

Resultados:

- Cantidad de útiles: 1000.
- Presupuesto: 10.000 Bs.
- Utilidad obtenida: 35.040.
- Tiempo de ejecución: 5,490969 segundos.

Esta prueba demuestra que la programación dinámica puede resolver una instancia considerablemente mayor que las utilizadas en la comparación con fuerza bruta.

## 6. ¿Qué sucede con un presupuesto de 1.000.000.000 Bs?

La programación dinámica implementada utiliza una tabla de dimensiones (n + 1) × (B + 1).

Por lo tanto, su complejidad temporal y espacial es O(n · B).

Si el presupuesto aumenta a 1.000.000.000 Bs, la tabla necesitaría una cantidad enorme de posiciones, lo que provocaría un consumo de memoria excesivo y un tiempo de ejecución impráctico.

Esto demuestra que la programación dinámica utilizada depende tanto de la cantidad de útiles como del valor numérico del presupuesto. Por esta razón, se considera una solución pseudo-polinomial y no resulta adecuada para presupuestos extremadamente grandes.

## 7. Conclusión

La comparación permitió comprobar que el algoritmo mejorado obtiene las mismas soluciones que el algoritmo ingenuo, pero con tiempos de ejecución considerablemente menores.

La fuerza bruta presenta un crecimiento exponencial, mientras que la programación dinámica presenta una complejidad O(n · B).

Por tanto, la programación dinámica resulta más conveniente para resolver el problema de selección de útiles cuando el presupuesto tiene un valor manejable.
