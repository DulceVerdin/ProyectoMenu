class AsignadorGrupos:
    def __init__(self):
        self.nombre = input("¿Cuál es tu nombre?: ")
        self.sexo = input("¿Cuál es tu sexo? (M para mujer, H para hombre): ").upper()

    def determinar_grupo(self):
        primera_letra = self.nombre[0].upper()
        es_mujer_grupo_a = (self.sexo == "M" and primera_letra < "M")
        es_hombre_grupo_a = (self.sexo == "H" and primera_letra > "N")
        
        if es_mujer_grupo_a or es_hombre_grupo_a:
            print("Perteneces al grupo A")
        else:
            print("Perteneces al grupo B")
