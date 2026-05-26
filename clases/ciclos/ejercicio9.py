class RepetidorPalabra:
    def __init__(self):
        self.palabra = input("Ingresa una palabra: ")

    def repetir(self, veces: int = 10):
        for i in range(1, veces + 1):
            print(f"{i}. {self.palabra}")