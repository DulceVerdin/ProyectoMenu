class Saludador:
    def __init__(self):
        self.nombre = input("Por favor, introduce tu nombre: ")

    def saludar(self):
        print(f"¡Hola {self.nombre}!")