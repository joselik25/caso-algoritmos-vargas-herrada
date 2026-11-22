JHONMAR VARGAS HERRADA

# Medición de tiempos

Se realizaron las pruebas con Python usando `time.perf_counter()` para medir el tiempo de ejecución.

Para cada tamaño se hizo una ejecución de calentamiento y después 3 mediciones. Se calculó el promedio de los tres tiempos.

## Gestor ingenuo

| Pacientes | Tiempo 1 (s) | Tiempo 2 (s) | Tiempo 3 (s) | Promedio (s) | Crecimiento |
|---:|---:|---:|---:|---:|---:|
| 2500 | 1.7070 | 1.5249 | 2.0050 | 1.7456 | - |
| 5000 | 4.6778 | 4.6447 | 4.3685 | 4.5636 | 2.61 |
| 10000 | 18.4231 | 17.6494 | 20.0519 | 18.7081 | 4.10 |

## Gestor mejorado

| Pacientes | Tiempo 1 (s) | Tiempo 2 (s) | Tiempo 3 (s) | Promedio (s) | Crecimiento |
|---:|---:|---:|---:|---:|---:|
| 2500 | 0.0085 | 0.0074 | 0.0092 | 0.0084 | - |
| 5000 | 0.0226 | 0.0188 | 0.0196 | 0.0203 | 2.42 |
| 10000 | 0.0484 | 0.0426 | 0.0437 | 0.0449 | 2.21 |

## Conclusiones

El gestor ingenuo presenta un crecimiento cercano a O(n²), porque debe recorrer la lista para encontrar al paciente con mayor prioridad. El gestor mejorado tiene un crecimiento mucho menor, correspondiente a las operaciones de la cola de prioridad O(log n). Las pequeñas diferencias entre mediciones pueden deberse a variaciones normales del equipo durante la ejecución.