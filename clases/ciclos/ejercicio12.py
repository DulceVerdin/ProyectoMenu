class CuentaAtras:
    def __init__(self):
        self.numero = int(input("Ingresa un número entero positivo: "))

    def iniciar_cuenta(self):
        numeros = []

        for i in range(self.numero, -1, -1):
            numeros.append(str(i))
            
        resultado = ", ".join(numeros)
        print(resultado)