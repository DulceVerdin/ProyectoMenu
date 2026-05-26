class PalabraInversa:
    def __init__(self):
        self.palabra = input("Introduce una palabra: ")

    def mostrar_al_reves(self):
        print("Letras al revés:")
        
        ultimo_indice = len(self.palabra) - 1
        
        for i in range(ultimo_indice, -1, -1):
            print(self.palabra[i])