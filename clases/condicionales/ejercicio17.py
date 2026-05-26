class DivisionSegura:
    def __init__(self):
        self.num1 = float(input("Introduce el primer número (dividendo): "))
        self.num2 = float(input("Introduce el segundo número (divisor): "))

    def realizar_division(self):
        if self.num2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = self.num1 / self.num2
            print(f"El resultado de la división es: {resultado}")