class TablasMultiplicar:
    def __init__(self, limite_tablas: int = 10, limite_multiplicador: int = 10):
        self.limite_tablas = limite_tablas
        self.limite_multiplicador = limite_multiplicador

    def generar_tablas(self):
        for numero in range(1, self.limite_tablas + 1):
            
            for i in range(1, self.limite_multiplicador + 1):
                prod = numero * i
                print(f"{numero} x {i} = {prod}")
          
            print()