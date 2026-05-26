class InversorFrase:
    def __init__(self):
        self.frase = input("Ingresa una frase: ")

    def obtener_invertida(self) -> str:
        return self.frase[::-1]

    def mostrar_resultado(self):
        print("Frase invertida:")
        print(self.obtener_invertida())