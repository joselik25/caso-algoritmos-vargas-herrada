# H3 - Comparación de algoritmos de optimización

## 1. Descripción del problema

Se plantea un problema de optimización relacionado con una tienda de tapices. Se dispone de una capacidad máxima de metros de tela y varios pedidos de corte.

Cada pedido debe seleccionarse completo o descartarse. El objetivo es aprovechar la mayor cantidad posible de metros sin superar la capacidad disponible.

Este es un ejercicio académico análogo al negocio, no un procedimiento que actualmente utilice la tienda.

## 2. Algoritmos implementados

### Fuerza bruta

Examina todas las combinaciones posibles de pedidos y conserva el mayor metraje que no supera la capacidad disponible.

Complejidad temporal: O(2^n), donde n es la cantidad de pedidos.

### Programación dinámica

Utiliza un arreglo para almacenar el mejor aprovechamiento posible para cada capacidad. Evalúa cada pedido una sola vez y actualiza los resultados evitando repetir cálculos.

Complejidad temporal: O(n × C), donde n es la cantidad de pedidos y C es la capacidad disponible.

## 3. Protocolo experimental

- Capacidad utilizada: 100 metros.
- Cantidades de pedidos evaluadas: 8, 12, 16 y 18.
- Los pedidos se generan aleatoriamente con valores enteros entre 1 y 30 metros.
- Se utiliza una semilla fija (2026 + cantidad de pedidos) para reproducir los mismos datos.
- Ambos algoritmos reciben exactamente los mismos pedidos.
- Se realiza una ejecución de calentamiento antes de medir.
- Se realizan tres mediciones por algoritmo.
- Se utiliza la mediana de los tiempos obtenidos.
- Se comprueba que ambos algoritmos devuelvan el mismo resultado.

Las mediciones se realizaron con `time.perf_counter()`.

## 4. Resultados experimentales

| Pedidos | Fuerza bruta (s) | Programación dinámica (s) | Resultado (m) |
|---:|---:|---:|---:|
| 8 | 0.00047460 | 0.00018210 | 97 |
| 12 | 0.01053900 | 0.00020700 | 100 |
| 16 | 0.16977280 | 0.00020360 | 100 |
| 18 | 0.74162990 | 0.00023120 | 100 |

## 5. Análisis de resultados

Los resultados muestran que ambos algoritmos encontraron el mismo aprovechamiento máximo en las cuatro pruebas.

Sin embargo, sus tiempos de ejecución presentan diferencias importantes.

La fuerza bruta aumenta considerablemente su tiempo al incrementar la cantidad de pedidos, debido a que examina todas las combinaciones posibles.

La programación dinámica mantiene tiempos de ejecución bajos en las pruebas realizadas, porque reutiliza los resultados almacenados en su arreglo.

## 6. Conclusión

En las cuatro pruebas realizadas, ambos algoritmos encontraron el mismo aprovechamiento máximo.

La fuerza bruta presentó un incremento considerable en su tiempo de ejecución al aumentar la cantidad de pedidos, debido a que evalúa todas las combinaciones posibles.

La programación dinámica obtuvo tiempos menores en las pruebas realizadas, reutilizando los resultados almacenados en su arreglo.

Por tanto, para el problema y las capacidades evaluadas, la programación dinámica resultó más eficiente que la fuerza bruta. Sin embargo, su rendimiento también depende de la capacidad disponible.