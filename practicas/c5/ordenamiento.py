import csv
import time
import random
import statistics
from pathlib import Path


RUTA_CSV = Path(__file__).resolve().parents[2] / "h1" / "datos.csv"


def cargar_inventario():
    with open(RUTA_CSV, "r", encoding="utf-8-sig", newline="") as archivo:
        return list(csv.DictReader(archivo))


# Algoritmo 1: Bubble Sort
def bubble_sort(datos):
    arreglo = datos.copy()
    n = len(arreglo)

    for i in range(n):
        intercambio = False

        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                intercambio = True

        if not intercambio:
            break

    return arreglo


# Algoritmo 2: Merge Sort
def merge_sort(datos):
    if len(datos) <= 1:
        return datos.copy()

    medio = len(datos) // 2
    izquierda = merge_sort(datos[:medio])
    derecha = merge_sort(datos[medio:])

    return mezclar(izquierda, derecha)


def mezclar(izquierda, derecha):
    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


# Algoritmo 3: Quick Sort
def quick_sort(datos):
    if len(datos) <= 1:
        return datos.copy()

    pivote = datos[len(datos) // 2]

    menores = [x for x in datos if x < pivote]
    iguales = [x for x in datos if x == pivote]
    mayores = [x for x in datos if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)


def medir(algoritmo, datos):
    algoritmo(datos)  # Calentamiento

    tiempos = []

    for _ in range(3):
        inicio = time.perf_counter()
        resultado = algoritmo(datos)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

        if resultado != sorted(datos):
            raise ValueError("El algoritmo produjo un orden incorrecto.")

    return statistics.mean(tiempos)


def main():
    base = cargar_inventario()
    tamanos = [500, 1000, 2000, 4000]

    algoritmos = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]

    print("TORNEO DE ALGORITMOS DE ORDENAMIENTO")
    print("-" * 75)
    print(f"{'Registros':<12}{'Bubble Sort':<20}"
          f"{'Merge Sort':<20}{'Quick Sort':<20}")
    print("-" * 75)

    for cantidad in tamanos:
        datos = [
            random.randint(1, cantidad * 10)
            for _ in range(cantidad)
        ]

        tiempos = []

        for nombre, algoritmo in algoritmos:
            tiempo = medir(algoritmo, datos)
            tiempos.append(tiempo)

        print(f"{cantidad:<12}{tiempos[0]:<20.8f}"
              f"{tiempos[1]:<20.8f}{tiempos[2]:<20.8f}")


if __name__ == "__main__":
    main()
