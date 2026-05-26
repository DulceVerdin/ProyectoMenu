class CalculadorPanaderia:
    def __init__(self):
        self.PRECIO_HABITUAL = 3.49
        self.DESCUENTO_PORCENTAJE = 0.60
        self.barras_no_frescas = int(input("¿Cuántas barras no frescas se vendieron?: "))

    def calcular_y_mostrar_recibo(self):
        precio_descuento = self.PRECIO_HABITUAL * self.DESCUENTO_PORCENTAJE
        precio_final_barra = self.PRECIO_HABITUAL - precio_descuento
        coste_total = self.barras_no_frescas * precio_final_barra

        print(f"\nPrecio habitual de una barra: {self.PRECIO_HABITUAL:.2f}€")
        print(f"Descuento por barra (60%): {precio_descuento:.2f}€")
        print(f"Precio final por barra: {precio_final_barra:.2f}€")
        print(f"Coste final total: {coste_total:.2f}€")