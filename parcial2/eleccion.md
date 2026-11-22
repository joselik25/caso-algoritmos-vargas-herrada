# JHONMAR VARGAS HERRADA

# P2.1 - Elección de estructuras de datos

## 1. Estructuras elegidas

Para resolver el sistema de turnos de la clínica elegí
utilizar dos estructuras de datos de Python:

- heapq: permite organizar los pacientes según su nivel
  de urgencia y su orden de llegada.
- set: permite consultar rápidamente si un paciente
  todavía se encuentra esperando.

La cola de prioridad utiliza dos criterios:
primero la urgencia y después el número de llegada.
Así se respeta el orden de atención solicitado.

## 2. Tabla de operaciones

| Operación | Cantidad diaria | Estructura | Costo |
|---|---:|---|---|
| Registrar | 100.000 | heapq + set | O(log n) |
| AtenderSiguiente | 100.000 | heapq + set | O(log n) |
| EstaEsperando | 30.000 | set | O(1) promedio |
| Esperando | Según consulta | len(heapq) | O(1) |

## 3. Comparación con la lista simple

Considerando n = 100.000 pacientes:

En la solución ingenua, para encontrar al paciente más
urgente se debe recorrer toda la lista.

Para atender a los 100.000 pacientes se realizan
aproximadamente:

100.000 x 99.999 / 2 = 4.999.950.000 comparaciones.

Además, eliminar un elemento de una lista puede requerir
desplazar los elementos restantes.

En la solución mejorada, registrar y atender utilizan
una cola de prioridad con costo O(log n).

Como log2(100.000) es aproximadamente 16,6,
las operaciones principales requieren mucho menos trabajo
que recorrer toda la lista.

Las consultas EstaEsperando utilizan un set, cuyo costo
promedio es O(1).

## 4. Condición para cambiar de opinión

Cambiaría mi elección si el sistema tuviera muy pocos
pacientes y casi ninguna operación de consulta.

En ese caso, una lista simple podría ser suficiente,
porque sería más sencilla de implementar y mantener.
