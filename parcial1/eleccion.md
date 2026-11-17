JHONMAR VARGAS HERRADA

# P1.3 - Elección del algoritmo para el inventario

## 1. Descripción del problema

El inventario contiene 250.000 códigos de productos que llegan desordenados cada mañana. Durante el día se realizan aproximadamente 8.000 consultas para buscar productos.

La memoria disponible es limitada, por lo que no se puede crear una copia adicional de toda la lista.

## 2. Comparación de alternativas

### Alternativa 1: Búsqueda lineal

Consiste en recorrer la lista hasta encontrar el código solicitado.

Complejidad por consulta: O(n).

En el peor caso:

250.000 × 8.000 = 2.000.000.000 comparaciones diarias.

Esta alternativa es sencilla, pero realiza demasiadas operaciones.

### Alternativa 2: Ordenamiento y búsqueda binaria

Primero se ordena la lista una vez y después se utiliza búsqueda binaria para cada consulta.

Ordenamiento aproximado:

250.000 × log2(250.000) ≈ 4.482.892 operaciones.

Búsquedas:

8.000 × 18 = 144.000 comparaciones aproximadamente.

Total aproximado:

4.482.892 + 144.000 = 4.626.892 operaciones.

Se puede ordenar la lista original en el mismo lugar para evitar almacenar una segunda copia.

### Alternativa 3: Ordenamiento cuadrático y búsqueda binaria

El ordenamiento cuadrático puede necesitar aproximadamente:

250.000² = 62.500.000.000 operaciones.

Después se realizan aproximadamente 144.000 comparaciones para las búsquedas binarias.

Esta alternativa resulta demasiado lenta para una lista de este tamaño.

## 3. Decisión

Se elige la alternativa 2: ordenar una vez la lista y utilizar búsqueda binaria.

Esta opción reduce considerablemente las operaciones necesarias para realizar las 8.000 consultas diarias. Además, se puede ordenar la lista original sin duplicarla, respetando la limitación de memoria.

## 4. Punto de cambio

Tomando el peor caso de la búsqueda lineal, cada consulta puede necesitar 250.000 comparaciones.

El ordenamiento cuesta aproximadamente 4.482.892 operaciones.

Por tanto, el punto de equilibrio es aproximadamente:

4.482.892 / 250.000 ≈ 18 consultas.

A partir de aproximadamente 18 consultas, ordenar y buscar mediante búsqueda binaria resulta más conveniente bajo esta estimación.

## 5. Conclusión

La búsqueda lineal puede ser útil cuando existen pocas consultas, porque no necesita ordenar los datos. Sin embargo, para 8.000 consultas diarias, ordenar una sola vez y utilizar búsqueda binaria resulta mucho más eficiente. Se recomienda esta alternativa porque reduce el tiempo de búsqueda y permite trabajar sobre la lista original sin duplicarla.

