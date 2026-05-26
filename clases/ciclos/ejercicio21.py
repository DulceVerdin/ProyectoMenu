class CalculadoraDivision:
    def __init__(self):
        self.n = int(input("Introduce el primer número entero (dividendo): "))
        self.m = int(input("Introduce el segundo número entero (divisor): "))

    def calcular_y_mostrar(self):
        cociente = self.n // self.m
        resto = self.n % self.m
        
        print(f"La división de {self.n} entre {self.m} da un cociente de {cociente} y un resto de {resto}.")