import math

class Sumatorias(object):

    def __init__(self):
        self.n = 0
        self.serie = 0

    def leerDatos(self):
        self.n = int(input('n='))

    def calcularSerie(self):
        self.serie = 0
        for i in range(1, self.n + 1):
            self.serie += 1 / math.sqrt((2 * i + 1) ** 2)

    def mostrarSerie(self):
        print(f"Serie = {self.serie}")