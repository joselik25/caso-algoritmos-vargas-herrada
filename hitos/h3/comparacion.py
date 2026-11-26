import random
import time
import statistics


def fuerza_bruta(pedidos, capacidad):
    mejor = 0
    n = len(pedidos)

    # Examina todas las combinaciones posibles.
    for mascara in range(1 << n):
        total = 0

        for i in range(n):
            if mascara & (1 << i):
                total += pedidos[i]

        if total <= capacidad and total > mejor:
            mejor = total

    return mejor


def programacion_dinamica(pedidos, capacidad):
    dp = [0] * (capacidad + 1)

    # Cada pedido se utiliza como máximo una vez.
    for metros in pedidos:
        for c in range(capacidad, metros - 1, -1):
            dp[c] = max(dp[c], dp[c - metros] + metros)

    return dp[capacidad]


def medir(funcion, pedidos, capacidad):
    tiempos = []

    # Calentamiento.
    funcion(pedidos, capacidad)

    # Tres mediciones.
    for _ in range(3):
        inicio = time.perf_counter()
        resultado = funcion(pedidos, capacidad)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return resultado, statistics.median(tiempos)


def main():
    capacidad = 100
    tamanos = [8, 12, 16, 18]

    print("COMPARACION: FUERZA BRUTA VS PROGRAMACION DINAMICA")
    print("-" * 85)
    print(f"{'Pedidos':<12}{'Fuerza bruta (s)':<22}"
          f"{'Prog. dinamica (s)':<23}{'Resultado':<12}")
    print("-" * 85)

    for n in tamanos:
        generador = random.Random(2026 + n)
        pedidos = [generador.randint(1, 30) for _ in range(n)]

        resultado_fb, tiempo_fb = medir(
            fuerza_bruta, pedidos, capacidad
        )

        resultado_pd, tiempo_pd = medir(
            programacion_dinamica, pedidos, capacidad
        )

        if resultado_fb != resultado_pd:
            raise ValueError("Los algoritmos no obtuvieron el mismo resultado.")

        print(f"{n:<12}{tiempo_fb:<22.8f}"
              f"{tiempo_pd:<23.8f}{resultado_pd:<12}")

    print("-" * 85)
    print("Todas las pruebas obtuvieron el mismo resultado.")


if __name__ == "__main__":
    main()
