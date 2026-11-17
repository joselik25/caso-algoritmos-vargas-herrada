JHONMAR VARGAS HERRADA

# P1.1 - Análisis de complejidad

## 1. Análisis de fragmentos

### F1
Complejidad: O(n).

Justificación: El algoritmo recorre el arreglo una sola vez, realizando una comprobación por cada elemento.

### F2
Complejidad: O(n²).

Justificación: Contiene dos ciclos anidados que recorren n elementos cada uno.

### F3
Complejidad: O(log n).

Justificación: La variable k se multiplica por 2 en cada iteración, reduciendo el número de repeticiones.

### F4
Complejidad: O(n log n).

Justificación: El ciclo exterior se ejecuta n veces y el ciclo interior divide k entre 3 en cada iteración.

## 2. Resolución de recurrencias

### Recurrencia 1

T(n) = 4T(n/3) + n

a = 4
b = 3
d = 1

Comparación:

b^d = 3^1 = 3

Como 4 es mayor que 3, la complejidad es:

T(n) = O(n^log₃(4))

### Recurrencia 2

T(n) = 2T(n/2) + n²

a = 2
b = 2
d = 2

Comparación:

b^d = 2² = 4

Como 2 es menor que 4, la complejidad es:

T(n) = O(n²)
