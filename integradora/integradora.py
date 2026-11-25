# JHONMAR VARGAS HERRADA

import random
import time


class CompradorMejorado:
    def __init__(self):
        self._elegidos = set()

    def Elegir(self, utiles, presupuesto):
        n = len(utiles)
        dp = [[0] * (presupuesto + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            costo = utiles[i - 1]["costo"]
            utilidad = utiles[i - 1]["utilidad"]

            for b in range(presupuesto + 1):
                dp[i][b] = dp[i - 1][b]

                if costo <= b:
                    alternativa = dp[i - 1][b - costo] + utilidad
                    if alternativa > dp[i][b]:
                        dp[i][b] = alternativa

        codigos = []
        b = presupuesto

        for i in range(n, 0, -1):
            if dp[i][b] != dp[i - 1][b]:
                codigos.append(utiles[i - 1]["codigo"])
                b -= utiles[i - 1]["costo"]

        codigos.reverse()
        self._elegidos = set(codigos)

        return dp[n][presupuesto], codigos

    def EstaEnLaCompra(self, codigo):
        return codigo in self._elegidos


class CompradorIngenuo:
    def __init__(self):
        self._elegidos = set()

    def Elegir(self, utiles, presupuesto):
        n = len(utiles)
        mejor_utilidad = 0
        mejor_mascara = 0

        for mascara in range(1 << n):
            costo = 0
            utilidad = 0

            for i in range(n):
                if mascara & (1 << i):
                    costo += utiles[i]["costo"]
                    utilidad += utiles[i]["utilidad"]

            if costo <= presupuesto and utilidad > mejor_utilidad:
                mejor_utilidad = utilidad
                mejor_mascara = mascara

        codigos = [
            utiles[i]["codigo"]
            for i in range(n)
            if mejor_mascara & (1 << i)
        ]

        self._elegidos = set(codigos)
        return mejor_utilidad, codigos

    def EstaEnLaCompra(self, codigo):
        return codigo in self._elegidos


def generar_utiles(n):
    azar = random.Random(n + 1000)

    return [
        {
            "codigo": f"K{i}",
            "costo": azar.randint(4, 49),
            "utilidad": azar.randint(10, 99)
        }
        for i in range(n)
    ]


def ejecutar_pruebas():
    comprador = CompradorMejorado()

    casos = [
        (
            "el voraz se equivoca",
            [
                {"codigo": "U1", "costo": 20, "utilidad": 120},
                {"codigo": "U2", "costo": 40, "utilidad": 200},
                {"codigo": "U3", "costo": 60, "utilidad": 240}
            ],
            100, 440, ["U2", "U3"]
        ),
        (
            "cuatro útiles",
            [
                {"codigo": "U1", "costo": 4, "utilidad": 6},
                {"codigo": "U2", "costo": 6, "utilidad": 8},
                {"codigo": "U3", "costo": 8, "utilidad": 10},
                {"codigo": "U4", "costo": 10, "utilidad": 12}
            ],
            16, 20, ["U2", "U4"]
        ),
        (
            "presupuesto cero",
            [
                {"codigo": "U1", "costo": 5, "utilidad": 10},
                {"codigo": "U2", "costo": 7, "utilidad": 12}
            ],
            0, 0, []
        ),
        ("sin útiles", [], 30, 0, []),
        (
            "ninguno cabe",
            [
                {"codigo": "U1", "costo": 80, "utilidad": 90},
                {"codigo": "U2", "costo": 100, "utilidad": 100}
            ],
            60, 0, []
        ),
        (
            "todos caben",
            [
                {"codigo": "U1", "costo": 10, "utilidad": 20},
                {"codigo": "U2", "costo": 14, "utilidad": 24},
                {"codigo": "U3", "costo": 6, "utilidad": 8}
            ],
            200, 52, ["U1", "U2", "U3"]
        )
    ]

    for nombre, utiles, presupuesto, esperada, codigos_esperados in casos:
        utilidad, codigos = comprador.Elegir(utiles, presupuesto)
        correcto = utilidad == esperada and codigos == codigos_esperados
        print(f"{nombre}: {'OK' if correcto else 'ERROR'}")
        print(f"  Utilidad: {utilidad} | Códigos: {codigos}")

    print("\nPruebas de búsqueda:")
    comprador.Elegir(casos[0][1], 100)
    print("U2 está en la compra:", comprador.EstaEnLaCompra("U2"))
    print("U1 está en la compra:", comprador.EstaEnLaCompra("U1"))


def ejecutar_carga(comprador, n):
    utiles = generar_utiles(n)
    presupuesto = sum(u["costo"] for u in utiles) // 3
    utilidad, _ = comprador.Elegir(utiles, presupuesto)
    return utilidad


def medir_algoritmo(nombre, clase_comprador, utiles, presupuesto):
    # Una ejecución de calentamiento
    clase_comprador().Elegir(utiles, presupuesto)

    tiempos = []
    utilidad_final = None

    for _ in range(3):
        comprador = clase_comprador()

        inicio = time.perf_counter()
        utilidad, _ = comprador.Elegir(utiles, presupuesto)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)
        utilidad_final = utilidad

    promedio = sum(tiempos) / 3

    print(f"{nombre}:")
    print("  Tiempos:", [round(t, 6) for t in tiempos])
    print(f"  Promedio: {promedio:.6f} segundos")
    print(f"  Utilidad: {utilidad_final}")

    return promedio, utilidad_final


def ejecutar_mediciones():
    print("\nMEDICIONES DE RENDIMIENTO")

    tamanos = [14, 16, 18, 20]
    anterior = None

    for n in tamanos:
        utiles = generar_utiles(n)
        presupuesto = sum(u["costo"] for u in utiles) // 3

        print(f"\n--- {n} útiles ---")

        tiempo_ingenuo, utilidad_ingenua = medir_algoritmo(
            "Ingenuo", CompradorIngenuo, utiles, presupuesto
        )

        tiempo_mejorado, utilidad_mejorada = medir_algoritmo(
            "Mejorado", CompradorMejorado, utiles, presupuesto
        )

        print("¿Misma utilidad?:", utilidad_ingenua == utilidad_mejorada)

        if anterior is not None:
            print(
                "Relación respecto al tamaño anterior:",
                round(tiempo_ingenuo / anterior, 2), "veces"
            )

        anterior = tiempo_ingenuo

    print("\nMEDICIÓN CON 1000 ÚTILES Y PRESUPUESTO 10000")

    utiles = generar_utiles(1000)
    comprador = CompradorMejorado()

    inicio = time.perf_counter()
    utilidad, _ = comprador.Elegir(utiles, 10000)
    fin = time.perf_counter()

    print("Utilidad:", utilidad)
    print("Tiempo:", round(fin - inicio, 6), "segundos")


if __name__ == "__main__":
    ejecutar_pruebas()
    ejecutar_mediciones()