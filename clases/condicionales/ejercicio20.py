class CalculadoraIMC:
    def __init__(self):
        self.peso = float(input("Peso (kg): "))
        self.estatura = float(input("Altura (mts): "))
        self.imc = 0.0

    def calcular_imc(self):
        self.imc = self.peso / (self.estatura ** 2)

    def obtener_diagnostico(self) -> str:
        if self.imc < 18.5:
            return "Bajo peso"
        elif 18.5 <= self.imc < 25.0:
            return "Normal"
        elif 25.0 <= self.imc < 30.0:
            return "Sobrepeso"
        else:
            return "Obesidad"

    def mostrar_reporte(self):
        self.calcular_imc()
        diagnostico = self.obtener_diagnostico()
        print(f"\nimc = {self.imc:.2f} - {diagnostico}")