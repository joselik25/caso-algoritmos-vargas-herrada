# JHONMAR VARGAS HERRADA
# Parcial 2 - Variante A

import heapq
import time


class GestorIngenuo:

    def __init__(self):
        self.lista = []
        self.llegadas = 0

    def registrar(self, nombre, urgencia):
        self.lista.append((nombre, urgencia, self.llegadas))
        self.llegadas += 1

    def atender_siguiente(self):
        if len(self.lista) == 0:
            return None

        mejor = 0

        for i in range(1, len(self.lista)):
            p = self.lista[i]
            m = self.lista[mejor]

            if p[1] < m[1] or (p[1] == m[1] and p[2] < m[2]):
                mejor = i

        nombre = self.lista[mejor][0]
        self.lista.pop(mejor)

        return nombre

    def esta_esperando(self, nombre):
        for p in self.lista:
            if p[0] == nombre:
                return True
        return False

    @property
    def esperando(self):
        return len(self.lista)


class GestorMejorado:

    def __init__(self):
        self.cola = []
        self.nombres = set()
        self.llegadas = 0

    def registrar(self, nombre, urgencia):
        heapq.heappush(self.cola, (urgencia, self.llegadas, nombre))
        self.nombres.add(nombre)
        self.llegadas += 1

    def atender_siguiente(self):
        if not self.cola:
            return None

        urgencia, llegada, nombre = heapq.heappop(self.cola)
        self.nombres.remove(nombre)

        return nombre

    def esta_esperando(self, nombre):
        return nombre in self.nombres

    @property
    def esperando(self):
        return len(self.cola)


def probar(titulo, gestor):

    guion = [
        ("registrar", "Ana", 3, ""),
        ("registrar", "Beto", 1, ""),
        ("registrar", "Carla", 3, ""),
        ("registrar", "Diego", 2, ""),
        ("esperando", "", 0, "4"),
        ("esta", "Beto", 0, "True"),
        ("esta", "Zoe", 0, "False"),
        ("atender", "", 0, "Beto"),
        ("esta", "Beto", 0, "False"),
        ("atender", "", 0, "Diego"),
        ("registrar", "Elena", 1, ""),
        ("atender", "", 0, "Elena"),
        ("atender", "", 0, "Ana"),
        ("atender", "", 0, "Carla"),
        ("atender", "", 0, "(nadie)"),
        ("esperando", "", 0, "0")
    ]

    bien = 0
    total = 0

    for op, arg, urg, esperado in guion:

        if op == "registrar":
            gestor.registrar(arg, urg)
            continue

        elif op == "atender":
            obtenido = gestor.atender_siguiente()
            if obtenido is None:
                obtenido = "(nadie)"

        elif op == "esta":
            obtenido = str(gestor.esta_esperando(arg))

        else:
            obtenido = str(gestor.esperando)

        total += 1

        if obtenido == esperado:
            bien += 1
        else:
            print("Error:", op, esperado, obtenido)

    print(titulo, bien, "de", total, "pasos correctos")


def ejecutar_carga(gestor, n):

    for i in range(n):
        urgencia = (i * 7919) % 5 + 1
        gestor.registrar("P" + str(i), urgencia)

    control = 0

    for i in range(n):
        nombre = gestor.atender_siguiente()
        control += len(nombre)

    return control


def medir(titulo, clase, tamanos):

    print("\n", titulo)

    promedios = []

    for n in tamanos:

        ejecutar_carga(clase(), n)

        tiempos = []

        for i in range(3):
            gestor = clase()

            inicio = time.perf_counter()
            ejecutar_carga(gestor, n)
            fin = time.perf_counter()

            tiempos.append(fin - inicio)

        promedio = sum(tiempos) / 3
        promedios.append(promedio)

        print("\nPacientes:", n)
        print("Tiempo 1:", round(tiempos[0], 4), "segundos")
        print("Tiempo 2:", round(tiempos[1], 4), "segundos")
        print("Tiempo 3:", round(tiempos[2], 4), "segundos")
        print("Promedio:", round(promedio, 4), "segundos")

    print("\nCrecimiento:")

    for i in range(1, len(promedios)):
        factor = promedios[i] / promedios[i - 1]
        print(round(factor, 2), "veces")


if __name__ == "__main__":

    probar("GestorIngenuo:", GestorIngenuo())
    probar("GestorMejorado:", GestorMejorado())

    tamanos = [2500, 5000, 10000]

    medir("GestorIngenuo", GestorIngenuo, tamanos)
    medir("GestorMejorado", GestorMejorado, tamanos)
