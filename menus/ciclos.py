from clases.ciclos.ejercicio10 import ContadorEdad
from clases.ciclos.ejercicio11 import ImparesConsecutivos
from clases.ciclos.ejercicio12 import CuentaAtras
from clases.ciclos.ejercicio13 import CalculadoraInversion
from clases.ciclos.ejercicio15 import PalabraInversa
from clases.ciclos.ejercicio16 import ContadorLetras
from clases.ciclos.ejercicio19 import Saludador
from clases.ciclos.ejercicio22 import CuentaAhorros
from clases.ciclos.ejercicio23 import CalculadorPanaderia
from clases.ciclos.ejercicio25 import InversorFrase
from clases.ciclos.ejercicio5 import Sumatorias
from clases.ciclos.ejercicio6 import calculadora
from clases.ciclos.ejercicio7 import Tabla
from clases.ciclos.ejercicio8 import TablasMultiplicar
from clases.ciclos.ejercicio9 import RepetidorPalabra
from clases.condicionales.ejercicio20 import CalculadoraIMC
class ciclos(object):
    def __init__(self):
        self.opcion=0

    def mostrar__menu__ciclos(self):
        print("--Menu ciclos--")
        print("1.sumatoria de una serie")
        print("2.calcular factorial")
        print("3.tabla de multiplicar")
        print("4.tablas de multiplicar del 1 al 10")
        print("5.repetir palabra")
        print("6.contar edades")
        print("7. numeros impares")
        print("8.cuenta atras")
        print("9.calculadora inversa")
        print("10.palabra inversa")
        print("11.contador de letras")
        print("12.saludo")
        print("13.divisor")
        print("14.ahorro")
        print("15.panaderia")
        print("16.frase invertida")
    
    
    def leer__ejecutar__opcion(self):
        self.opcion = int(input("Selecciona una opcion"))
        match self.opcion:
            case 1:
                suma = Sumatorias()
                suma.leerDatos()
                suma.calcularSerie()
                suma.mostrarSerie()
            case 2:
                figura = calculadora(0)
                figura.leer_datos()
                figura.imprimir_serie()
            case 3:
                  mi_tabla = Tabla(0)
                  mi_tabla.leer_datos()
                  mi_tabla.calcular_tabla()
            case 4:
                  tablas = TablasMultiplicar()
                  tablas.generar_tablas()
            case 5:
                programa = RepetidorPalabra()
                programa.repetir()
            case 6: 
                programa= ContadorEdad()
                programa.mostrar_anios_cumplidos()
            case 7:
                programa = ImparesConsecutivos()
                programa.mostrar_impares()
            case 8:
                programa= CuentaAtras()
                programa.iniciar_cuenta()
            case 9:
                programa= CalculadoraInversion()
                programa.calcular_rendimientos()
            case 10:
                programa= PalabraInversa()
                programa.mostrar_al_reves()
            case 11:
                programa = ContadorLetras()
                programa.mostrar_resultado()
            case 12:
                programa = Saludador()
                programa.saludar()
            case 13:
                programa= CalculadoraIMC()
                programa.mostrar_reporte()
            case 14:
                programa= CuentaAhorros()
                programa.calcular_progresion()
            case 15:
                programa= CalculadorPanaderia()
                programa.calcular_y_mostrar_recibo()
            case 16:
                programa = InversorFrase()
                programa.mostrar_resultado()
    def ejecutar(self):
        while self.opcion != 16:
            self.mostrar__menu__ciclos()
            self.leer__ejecutar__opcion()

        
        
        