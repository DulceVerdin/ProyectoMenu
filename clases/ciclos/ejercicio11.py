class ImparesConsecutivos:
    def __init__(self):
        self.numero = int(input("Ingresa un número entero positivo: "))

    def mostrar_impares(self):
        impares = []
        
        for i in range(1, self.numero + 1, 2):
            impares.append(str(i))
            
        resultado = ", ".join(impares)
        print(resultado)