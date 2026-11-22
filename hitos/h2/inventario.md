# H2 – Inventario del caso real

## 1. Descripción del caso

El caso corresponde a una tienda dedicada a la venta de tapices y telas para tapicería. El control de inventario se realiza mediante Microsoft Excel, donde cada rollo se registra individualmente.

Cada rollo tiene un identificador único y se controlan sus características, metraje disponible y ubicación. No se deben combinar rollos del mismo color, porque pueden pertenecer a diferentes lotes.

## 2. Datos registrados

Cada registro contiene los siguientes campos:

- ID Rollo: identificador único del rollo.
- SKU: código del producto.
- Tejido: tipo de tela.
- Color: color del material.
- Lote: identificación del lote.
- Ancho: ancho de la tela.
- Metros Iniciales: cantidad inicial del rollo.
- Metros Cortados: cantidad retirada mediante cortes.
- Merma: cantidad de material defectuoso.
- Stock Actual: metros disponibles.
- Ubicación: lugar donde se encuentra el rollo.

El stock actual se calcula restando los metros cortados y la merma a los metros iniciales.

## 3. Operaciones del inventario

El sistema de inventario debe permitir las siguientes operaciones:

1. **Buscar por clave:** localizar un rollo mediante su ID Rollo.
2. **Insertar:** registrar un nuevo rollo cuando ingresa mercadería.
3. **Eliminar:** retirar un registro cuando un rollo deja de formar parte del inventario.
4. **Consultar mínimo:** identificar el rollo con menor cantidad de metros disponibles.
5. **Consultar sucesor:** encontrar el siguiente registro según un orden establecido.
6. **Consultar rangos:** localizar rollos cuyo stock se encuentre dentro de un intervalo de metros.
7. **Recorrido ordenado:** mostrar los rollos ordenados por un criterio, como ID Rollo o Stock Actual.
8. **Actualizar existencias:** descontar los metros cortados y registrar la merma.
9. **Controlar retazos:** identificar rollos con menos de 2,5 metros disponibles para trasladarlos a la zona de retazos.

## 4. Operaciones más frecuentes

De acuerdo con el funcionamiento descrito por la tienda, las operaciones principales son:

- Buscar rollos para verificar sus características y disponibilidad.
- Consultar el stock actual antes de realizar una venta o un corte.
- Actualizar los metros disponibles después de cada corte.
- Registrar la merma cuando se detecta material defectuoso.
- Consultar la ubicación de cada rollo.

La búsqueda y actualización de existencias son operaciones importantes porque se realizan durante el movimiento habitual de mercadería.

## 5. Volumen de datos

Se estima que el inventario puede contener 200 rollos o más. Esta cantidad es aproximada, ya que no se dispone de un conteo exacto.

Durante la experiencia laboral, algunas búsquedas podían tardar aproximadamente entre 5 y 10 minutos.

