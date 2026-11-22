import time
import statistics
import csv
from pathlib import Path


RUTA_CSV = Path(__file__).resolve().parents[2] / "h1" / "datos.csv"


def cargar_datos():
    with open(RUTA_CSV, "r", encoding="utf-8-sig", newline="") as archivo:
        return list(csv.DictReader(archivo))


def generar_inventario(cantidad):
    base = cargar_datos()
    inventario = []

    for i in range(cantidad):
        registro = base[i % len(base)].copy()
        registro["ID_Rollo"] = f"R-{i + 1:06d}"
        inventario.append(registro)

    return inventario


def buscar_lineal(inventario, id_buscado):
    for rollo in inventario:
        if rollo["ID_Rollo"] == id_buscado:
            return rollo
    return None


def buscar_hash(diccionario, id_buscado):
    return diccionario.get(id_buscado)


def medir(funcion, datos, id_buscado, repeticiones=10000):
    # Calentamiento
    funcion(datos, id_buscado)

    tiempos = []
    resultado = None

    for _ in range(3):
        inicio = time.perf_counter()

        for _ in range(repeticiones):
            resultado = funcion(datos, id_buscado)

        fin = time.perf_counter()
        tiempos.append((fin - inicio) / repeticiones)

    return statistics.mean(tiempos), resultado


def main():
    tamanos = [500, 1000, 2000, 4000]

    print("COMPARACION: BUSQUEDA LINEAL VS TABLA HASH")
    print("-" * 105)
    print(
        f"{'Registros':<12}"
        f"{'Lineal (s)':<20}"
        f"{'Hash (s)':<20}"
        f"{'Lineal/Hash':<18}"
        f"{'Crec. lineal':<17}"
        f"{'Crec. hash':<17}"
    )
    print("-" * 105)

    tiempo_lineal_anterior = None
    tiempo_hash_anterior = None

    for cantidad in tamanos:
        inventario = generar_inventario(cantidad)

        diccionario = {
            rollo["ID_Rollo"]: rollo
            for rollo in inventario
        }

        id_buscado = f"R-{cantidad:06d}"

        tiempo_lineal, resultado_lineal = medir(
            buscar_lineal, inventario, id_buscado
        )

        tiempo_hash, resultado_hash = medir(
            buscar_hash, diccionario, id_buscado
        )

        if resultado_lineal != resultado_hash:
            raise ValueError("Los resultados de las búsquedas no coinciden.")

        relacion = tiempo_lineal / tiempo_hash

        if tiempo_lineal_anterior is None:
            crecimiento_lineal_texto = "-"
            crecimiento_hash_texto = "-"
        else:
            crecimiento_lineal = tiempo_lineal / tiempo_lineal_anterior
            crecimiento_hash = tiempo_hash / tiempo_hash_anterior

            crecimiento_lineal_texto = f"{crecimiento_lineal:.2f}"
            crecimiento_hash_texto = f"{crecimiento_hash:.2f}"

        print(
            f"{cantidad:<12}"
            f"{tiempo_lineal:<20.10f}"
            f"{tiempo_hash:<20.10f}"
            f"{relacion:<18.2f}"
            f"{crecimiento_lineal_texto:<17}"
            f"{crecimiento_hash_texto:<17}"
        )

        tiempo_lineal_anterior = tiempo_lineal
        tiempo_hash_anterior = tiempo_hash

    print("-" * 105)
    print("Todas las búsquedas encontraron el mismo registro.")


if __name__ == "__main__":
    main()
