import math

class calculadora:
    def __init__(self, n):
        self.n = n

    def leer_datos(self):
        self.n = int(input('n = '))

    def calcular_serie(self):
        serie = 0
        for k in range(1, self.n + 1):
            serie += (1 / math.e)**k

        resultado_final = (1/3) * serie
        return resultado_final

    def imprimir_serie(self):
        print(f'serie = {self.calcular_serie()}')