JHONMAR VARGAS HERRADA

# P1.2 - Corrección y medición

## 1. Objetivo

El objetivo es mejorar el método que busca comprobantes repetidos y comparar su tiempo de ejecución con el método original.

## 2. Métodos utilizados

### Método original

Compara cada comprobante con todos los que le siguen para detectar valores repetidos.

Complejidad: O(n²).

### Método mejorado

Se utiliza HashSet para almacenar los comprobantes encontrados y detectar si un valor ya existe.

Complejidad promedio: O(n).

El método mejorado no modifica el arreglo original.

## 3. Casos de prueba

Se realizaron cinco pruebas:

1. Repetido en el medio.
2. Sin repetidos.
3. Lista vacía.
4. Un solo elemento.
5. Repetido en los extremos.

Resultado: los cinco casos fueron correctos.

## 4. Protocolo de medición

Se utilizaron datos sin repetidos generados mediante GenerarSinRepetidos(n, 77).

Se probaron cuatro tamaños: 5.000, 10.000, 20.000 y 40.000 elementos.

Para cada tamaño se realizó un calentamiento y tres ejecuciones medidas. Se calculó el promedio de los tres tiempos.

## 5. Resultados

| Tamaño | Original (ms) | Mejorado (ms) |
|---|---:|---:|
| 5.000 | 25,667 | 0,000 |
| 10.000 | 124,667 | 0,000 |
| 20.000 | 427,000 | 1,000 |
| 40.000 | 1791,000 | 2,333 |

## 6. Comparación

El método original aumenta considerablemente su tiempo cuando crece la cantidad de comprobantes. El método mejorado mantiene tiempos mucho menores.

Los valores de 0,000 ms indican que el tiempo fue inferior a la precisión de la medición en milisegundos.

## 7. Conclusión

La versión mejorada presenta un rendimiento superior al método original. Esto se debe a que utiliza HashSet para detectar repetidos sin comparar todos los elementos entre sí. Por esta razón, se considera una alternativa más eficiente para trabajar con grandes cantidades de comprobantes.

