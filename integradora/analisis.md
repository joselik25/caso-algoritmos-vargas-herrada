JHONMAR VARGAS HERRADA

# I1. Análisis del problema

## a) Complejidad del algoritmo CompradorIngenuo

El método `Elegir` de CompradorIngenuo tiene una complejidad temporal de O(n · 2^n).

Esto se debe a que el algoritmo genera todas las combinaciones posibles de útiles mediante una máscara binaria. Para n útiles existen 2^n combinaciones.

Además, para cada combinación recorre los n útiles para calcular el costo y la utilidad total. Por esta razón, el costo total es O(n · 2^n).

Este algoritmo es correcto porque revisa todas las combinaciones posibles, pero resulta lento cuando aumenta la cantidad de útiles.

## b) Análisis de la recurrencia

La recurrencia planteada es:

T(n) = 2T(n-1) + 1

Esta expresión representa un proceso que genera dos subproblemas de tamaño n-1 y realiza un trabajo adicional constante.

Al desarrollar la recurrencia:

T(n) = 2T(n-1) + 1

T(n) = 2[2T(n-2) + 1] + 1

T(n) = 4T(n-2) + 3

Continuando el desarrollo, se obtiene un crecimiento exponencial de Θ(2^n).

El Teorema Maestro básico no se aplica directamente porque su forma estándar utiliza subproblemas de tamaño n/b, mientras que aquí el tamaño disminuye de n a n-1.

Por tanto, la recurrencia se resuelve mediante expansión o árbol de recursión.

## c) Evaluación de la estrategia voraz y estrategia elegida

Una estrategia voraz consiste en seleccionar primero los elementos que parecen ofrecer el mayor beneficio según un criterio, como la utilidad dividida entre el costo.

Sin embargo, esta estrategia no garantiza encontrar la mejor combinación.

En el primer caso de prueba se tienen los siguientes útiles:

- U1: costo 20 Bs y utilidad 120.
- U2: costo 40 Bs y utilidad 200.
- U3: costo 60 Bs y utilidad 240.
- Presupuesto: 100 Bs.

Las relaciones de utilidad por costo son:

- U1: 6.
- U2: 5.
- U3: 4.

Si se utiliza el criterio voraz de mayor utilidad por costo, primero se selecciona U1 y después U2. Se obtiene una utilidad de 320, pero ya no queda presupuesto suficiente para U3.

En cambio, seleccionando U2 y U3 se obtiene un costo total de 100 Bs y una utilidad de 440. Esta es la combinación óptima.

Por este motivo, se eligió la programación dinámica para resolver el problema. Esta estrategia evalúa las mejores soluciones de subproblemas y permite encontrar la combinación óptima sin revisar todas las combinaciones posibles.

El problema presenta subproblemas repetidos porque diferentes combinaciones pueden necesitar calcular la mejor utilidad disponible para una misma cantidad de útiles y presupuesto restante.

La complejidad temporal de la programación dinámica implementada es O(n · B), donde n representa la cantidad de útiles y B representa el presupuesto. Su complejidad espacial es O(n · B), debido a la tabla utilizada para almacenar los resultados.

## d) Estructura de datos para EstaEnLaCompra

Para el método `EstaEnLaCompra` se eligió utilizar un conjunto (`set`).

Esta estructura permite almacenar los códigos de los útiles seleccionados y consultar si un código existe en el conjunto.

La búsqueda promedio tiene una complejidad de O(1), porque utiliza una tabla hash.

En cambio, si se utilizara una lista, la búsqueda tendría una complejidad de O(n) en el peor caso, ya que sería necesario recorrer sus elementos hasta encontrar el código o confirmar que no existe.

Por lo tanto, el conjunto permite realizar las consultas de pertenencia de manera más eficiente.
