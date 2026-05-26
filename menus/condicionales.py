from clases.condicionales.ejercicio4 import Circunferencia
from clases.condicionales.ejercicio14 import VerificadorPrimos
from clases.condicionales.ejercicio17 import DivisionSegura
from clases.condicionales.ejercicio18 import AsignadorGrupos
from clases.condicionales.ejercicio20 import CalculadoraIMC
from clases.condicionales.ejercicio24 import TaquillaSalaJuegos
class condicionales(object):
    def __init__(self):
        self.opcion=0

    def mostrar__menu__condicionales(self):
        print("--Menu condicionales--")
        print("1.circunferencia")
        print("2.Numeros primos")
        print("3.Divisiones")
        print("4.asignacion de grupo ")
        print("5.calculadora IMC")
        print("6.taquilla sala de juegos")
    
    def leer__ejecutar__opcion(self):
        self.opcion = int(input("Selecciona una opcion"))
        match self.opcion:
            case 1:
                figura = Circunferencia(0, 0, 0)
                figura.leer_datos()
                figura.imprimir_resultado(0, 0)
                
            case 2:
                programa = VerificadorPrimos()
                programa.mostrar_resultado()

            case 3:
                 programa = DivisionSegura()
                 programa.realizar_division()

            case 4:
                programa= AsignadorGrupos()
                programa.determinar_grupo()

            case 5:
                programa= CalculadoraIMC()
                programa.mostrar_reporte()

            case 6:
                sala_juegos = TaquillaSalaJuegos()
                sala_juegos.mostrar_ticket()

            case 7:
                pass
    def ejecutar(self):
        while self.opcion != 7:
            self.mostrar__menu__basicos()
            self.leer__ejecutar__opcion()
             