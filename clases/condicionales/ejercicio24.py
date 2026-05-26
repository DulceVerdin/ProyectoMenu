class TaquillaSalaJuegos:
    def __init__(self):
        self.edad = int(input("Introduce la edad del cliente: "))
        self.precio_entrada = 0

    def calcular_precio(self):
        if self.edad < 4:
            self.precio_entrada = 0
        elif 4 <= self.edad <= 18:
            self.precio_entrada = 5
        else:
            self.precio_entrada = 10

    def mostrar_ticket(self):
        self.calcular_precio()
        
        if self.precio_entrada == 0:
            print("El cliente puede entrar gratis.")
        else:
            print(f"El precio de la entrada es: {self.precio_entrada}€")