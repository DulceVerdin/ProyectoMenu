class ContadorLetras:
    def __init__(self):
        self.frase = input("Ingresa una frase: ")
        self.letra_buscada = input("Ingresa una letra: ")

    def contar_letra(self) -> int:
        contador = 0
        
        for letra in self.frase:
            if letra == self.letra_buscada:
                contador += 1
                
        return contador

    def mostrar_resultado(self):
        total = self.contar_letra()
        print(f"La letra '{self.letra_buscada}' aparece {total} veces en la frase.")