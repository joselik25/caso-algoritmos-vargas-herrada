import csv
import time
import statistics
from pathlib import Path

RUTA_CSV = Path(__file__).resolve().parents[2] / "h1" / "datos.csv"


def cargar_inventario():
    with open(RUTA_CSV, "r", encoding="utf-8-sig", newline="") as archivo:
        return list(csv.DictReader(archivo))


def busqueda_lineal(inventario, id_buscado):
    for rollo in inventario:
        if rollo["ID_Rollo"] == id_buscado:
            return rollo
    return None


def busqueda_binaria(inventario, id_buscado):
    izquierda = 0
    derecha = len(inventario) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        id_actual = inventario[medio]["ID_Rollo"]

        if id_actual == id_buscado:
            return inventario[medio]
        elif id_actual < id_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None


def crear_datos(base, cantidad):
    datos = []

    for i in range(cantidad):
        original = base[i % len(base)].copy()
        original["ID_Rollo"] = f"R-{i + 1:06d}"
        datos.append(original)

    return datos


def medir(funcion, datos, id_buscado):
    funcion(datos, id_buscado)  # Calentamiento

    tiempos = []

    for _ in range(3):
        inicio = time.perf_counter()
        funcion(datos, id_buscado)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)

    return statistics.mean(tiempos)


def main():
    base = cargar_inventario()
    tamanos = [500, 1000, 2000, 4000]

    print("COMPARACION DE BUSQUEDA LINEAL Y BINARIA")
    print("-" * 95)
    print(f"{'Registros':<12}{'Lineal (s)':<20}{'Binaria (s)':<20}"
          f"{'Lineal/Binaria':<20}")
    print("-" * 95)

    for cantidad in tamanos:
        datos = crear_datos(base, cantidad)
        datos_ordenados = sorted(
            datos, key=lambda rollo: rollo["ID_Rollo"]
        )

        # Buscar el ultimo registro para exigir un recorrido largo
        id_buscado = datos[-1]["ID_Rollo"]

        tiempo_lineal = medir(busqueda_lineal, datos, id_buscado)
        tiempo_binario = medir(
            busqueda_binaria, datos_ordenados, id_buscado
        )

        relacion = tiempo_lineal / tiempo_binario

        print(f"{cantidad:<12}{tiempo_lineal:<20.10f}"
              f"{tiempo_binario:<20.10f}{relacion:.2f} veces")


if __name__ == "__main__":
    main()