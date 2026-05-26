from clases.basicos.ejercicio1 import Recta
from clases.basicos.ejercicio2 import Coordenadas
from clases.basicos.ejercicio3 import Funcion

class basicos(object):
    def __init__(self):
        self.opcion=0

    def mostrar__menu__basicos(self):
        print("--Menu basicos--")
        print("1.Pendiente de una recta")
        print("2.Distancia entre 2 puntos")
        print("3.Calcular funcion")
        print("4.volver al menu principal")
    
    def leer__ejecutar__opcion(self):
        self.opcion = int(input("Selecciona una opcion"))
        match self.opcion:
            case 1:
                figura = Recta(0, 0, 0, 0)
                figura.leer_datos()
                figura.calcular_pendiente()
                figura.imprimir_pendiente()
            case 2:
                puntos = Coordenadas()
                puntos.leerDatos
                puntos.calcularDistancia()
                puntos.imprimirDistancia()

            case 3:
                  figura = Funcion 
                  figura.leer_datos()
                  figura.calcular_fx()
                  figura.imprimir_fx()
            case 4:
                  pass
            
    def ejecutar(self):
        while self.opcion != 4:
            self.mostrar__menu__basicos()
            self.leer__ejecutar__opcion()

        
        
        