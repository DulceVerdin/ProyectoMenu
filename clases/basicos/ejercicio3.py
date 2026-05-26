import math
class Funcion:
    def __init__(self, x, mu, sigma):
        self.x = x
        self.mu = mu
        self.sigma = sigma

    def leer_datos(self):
        self.x = float(input('x = '))
        self.mu = float(input('mu = '))
        self.sigma = float(input('sigma = '))

    def calcular_fx(self):
        if self.sigma == 0:
            return 0

        exponente = -0.5 * ((self.x - self.mu) / self.sigma) ** 2
        denominador = self.sigma * math.sqrt(2 * math.pi)
        fx = (1 / denominador) * math.exp(exponente)

        return fx

    def imprimir_fx(self):
        # Llamamos al método que hace el cálculo y guardamos el resultado
        resultado = self.calcular_fx()
        print(f'fx = {resultado}')
