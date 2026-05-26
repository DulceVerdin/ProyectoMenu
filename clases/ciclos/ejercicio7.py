class Tabla:
    def __init__(self, numero=0):
        self.numero = numero

    def leer_datos(self):
        self.numero = int(input('Número = '))

    def calcular_tabla(self):
        print(f"\nTabla del {self.numero}:")
        for i in range(1, 11):
            resultado = self.numero * i
            print(f"{self.numero} x {i} = {resultado}")