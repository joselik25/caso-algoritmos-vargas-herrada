# H2 – Selección de estructuras de datos

## 1. Estructuras seleccionadas

Para administrar el inventario de rollos de tela se propone utilizar una tabla hash y un árbol AVL. Cada estructura atenderá operaciones diferentes.

### 1.1. Tabla hash (diccionario)

La tabla hash almacenará los registros utilizando el campo `ID_Rollo` como clave única.

Esta estructura permitirá localizar rápidamente un rollo para consultar sus características o actualizar sus existencias después de un corte o una merma.

### 1.2. Árbol AVL

El árbol AVL almacenará los rollos ordenados mediante una clave compuesta por `Stock Actual` e `ID_Rollo`.

Se utilizará para consultar el rollo con menor stock, encontrar el siguiente registro, consultar intervalos de existencias y recorrer los registros en orden.

La clave compuesta permite distinguir rollos que tengan la misma cantidad de metros disponibles.

## 2. Costos de las operaciones

| Operación | Tabla hash | Árbol AVL |
|---|---|---|
| Buscar por ID | O(1) promedio | O(log n) |
| Insertar | O(1) promedio | O(log n) |
| Eliminar | O(1) promedio | O(log n) |
| Consultar mínimo | O(n) | O(log n) |
| Consultar sucesor | O(n) | O(log n) |
| Consultar rango | O(n) | O(log n + k) |
| Recorrido ordenado | O(n log n) si se ordena | O(n) |

Donde:

- `n` representa la cantidad de rollos registrados.
- `k` representa la cantidad de resultados encontrados en una consulta por rango.
- Los costos de la tabla hash son promedios; en el peor caso, algunas operaciones pueden llegar a O(n).

## 3. Justificación

La tabla hash se selecciona porque la búsqueda por identificador es una operación frecuente en el inventario. Su costo promedio O(1) permite localizar un rollo sin recorrer todos los registros.

El árbol AVL complementa la tabla hash porque mantiene los registros ordenados y permite realizar consultas de mínimo, sucesor y rango con costos eficientes.

Ambas estructuras se complementan: la tabla hash facilita el acceso directo por identificador y el árbol AVL permite consultas ordenadas por cantidad de metros disponibles.

## 4. Conclusión

La combinación de una tabla hash y un árbol AVL permite atender tanto las búsquedas directas como las consultas ordenadas del inventario. Esta propuesta busca reducir el tiempo necesario para localizar rollos y consultar sus existencias.