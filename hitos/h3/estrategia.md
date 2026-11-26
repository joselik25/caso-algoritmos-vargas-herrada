# H3 - Análisis de estrategias de optimización

## 1. Descripción del problema

En el contexto de una tienda de tapices se plantea un problema de optimización análogo al aprovechamiento del metraje disponible de un rollo.

Se dispone de una capacidad máxima de metros y de varios pedidos de corte. Cada pedido tiene una cantidad de metros determinada y debe seleccionarse completo o descartarse.

El objetivo es seleccionar una combinación de pedidos que aproveche la mayor cantidad posible de metros sin superar la capacidad disponible.

Este planteamiento es un ejercicio académico de optimización y no representa el procedimiento habitual de atención de pedidos de la tienda.

## 2. Análisis de la estrategia voraz (Greedy)

Una estrategia voraz toma decisiones locales buscando la opción que parece más conveniente en cada paso.

Para este problema se puede plantear la regla de seleccionar primero el pedido con mayor cantidad de metros.

Sin embargo, esta regla no garantiza una solución óptima.

### Contraejemplo

Capacidad disponible: 20 metros.

Pedidos: 12, 11 y 9 metros.

La estrategia voraz selecciona primero el pedido de 12 metros. Los pedidos restantes ya no caben, por lo que obtiene un resultado de 12 metros.

Sin embargo, la combinación de 11 + 9 metros utiliza exactamente los 20 metros disponibles.

Por tanto, la estrategia voraz basada en seleccionar primero el pedido más grande no garantiza el aprovechamiento máximo.

## 3. Análisis de programación dinámica

La programación dinámica es adecuada para este problema porque permite resolver subproblemas y reutilizar sus resultados.

Se puede calcular el mejor aprovechamiento posible para cada capacidad, considerando si cada pedido se incluye o no en la solución.

Cada pedido se considera una sola vez, por lo que se trata de un problema de selección 0/1.

La estrategia permite encontrar la combinación óptima sin generar repetidamente todas las combinaciones posibles.

## 4. Estrategia seleccionada

Se selecciona programación dinámica porque garantiza encontrar el máximo metraje aprovechado sin superar la capacidad disponible.

La fuerza bruta se utilizará como método de referencia para comparar los resultados y medir el rendimiento de ambas soluciones.

## 5. Complejidad

- Fuerza bruta: O(2^n), porque evalúa todas las combinaciones posibles de pedidos.
- Programación dinámica: O(n × C), donde n es la cantidad de pedidos y C es la capacidad disponible expresada en unidades enteras de metros.

La programación dinámica reduce el trabajo computacional cuando la cantidad de pedidos aumenta, aunque su rendimiento también depende del valor de la capacidad.
