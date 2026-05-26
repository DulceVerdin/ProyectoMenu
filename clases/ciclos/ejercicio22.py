class CuentaAhorros:
    def __init__(self):
        self.ahorro = float(input("¿Cantidad de ahorro inicial?: "))
        self.tasa_interes = 0.04  

    def calcular_progresion(self, años: int = 3):
        balance = self.ahorro
        print("\n--- Evolución del Saldo ---")
        
        for i in range(1, años + 1):
            balance += balance * self.tasa_interes
            print(f"Balance tras el año {i}: {balance:.2f}")