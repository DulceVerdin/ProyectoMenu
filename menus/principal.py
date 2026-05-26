from menus.basicos import basicos
from menus.condicionales import condicionales
from menus.ciclos import ciclos

class Principal(object):
    def __init__(self):
        self.opcion = 0

    def __init__(self):
        print("---Menu Principal---")
        print("1. Basicos")
        print("2. Ciclos")
        print("3. Condicionales")
        #pendiente de agregar opciones para cada tema
        print("5.Salir")

    def leer__ejecutar__opcion (self):
        self.opcion = int(input("Seleccione una opcion:"))
        match self.opcion:
            case 1:
                Basicos = basicos()
                Basicos.ejecutar()
            case 2:
                Condicionales = condicionales()
                Condicionales.ejecutar()
            case 3:
                Ciclos = ciclos()
                Ciclos.ejecutar()
            case 4:
                pass

    def ejecutar(self):
        while self.opcion != 5:
            self.mostrar__menu__principal()
            self.leer__ejecutar__opcion