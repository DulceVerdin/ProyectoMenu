class Circunferencia:
    def __init__(self, x_centro, y_centro, radio):
        self.x_centro = x_centro
        self.y_centro = y_centro
        self.radio = radio
    def leer_datos(self):
        self.x_centro = float(input('x centro: '))
        self.y_centro = float(input('y centro: '))
        self.radio = float(input('radio: '))
    def calcular_distancia(self, x_punto, y_punto):
        return ((x_punto - self.x_centro)**2 + (y_punto - self.y_centro)**2)**0.5

    def imprimir_resultado(self, x_punto, y_punto):
        distancia = self.calcular_distancia(x_punto, y_punto)

        if distancia > self.radio:
            print(f'Resultado: El punto está fuera de la circunferencia')
        elif distancia < self.radio:
            print(f'Resultado: El punto está dentro de la circunferencia')
        else:
            print(f'Resultado: El punto está sobre la circunferencia')