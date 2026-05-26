class ContadorEdad:
    def __init__(self):
        self.edad = int(input("¿Cuál es tu edad?: "))

    def mostrar_anios_cumplidos(self):
        for i in range(1, self.edad + 1):
            if i == 1:
                print(f"Has cumplido {i} año")
            else:
                print(f"Has cumplido {i} años")