class VerificadorPrimos:
    def __init__(self):
        self.numero = int(input("Introduce un número entero: "))

    def es_primo(self) -> bool:
        if self.numero <= 1:
            return False
            
        for i in range(2, self.numero):
            if self.numero % i == 0:
                return False 
                
        return True 

    def mostrar_resultado(self):
        if self.es_primo():
            print(f"El número {self.numero} es primo.")
        else:
            print(f"El número {self.numero} no es primo.")