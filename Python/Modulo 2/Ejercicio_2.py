class CuentaBancaria:
    def __init__(self, numero_cuenta : str, titular : str, saldo :int):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se depositaron {cantidad} pesos en la cuenta. Saldo actual: {self.saldo} pesos.")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se retiraron {cantidad} pesos de la cuenta. Saldo actual: {self.saldo} pesos.")

        else:
            print(f"No hay suficiente saldo en la cuenta.")
    
    def mostrar_saldo(self):
        print(f"El saldo de la cuenta es: {self.saldo} pesos.")

cuenta1 = CuentaBancaria("123456789", "Juan Pérez", 1000)
cuenta2 = CuentaBancaria("987654321", "María López", 500)

cuenta1.depositar(500)
cuenta2.retirar(200)

cuenta1.mostrar_saldo()
cuenta2.mostrar_saldo()
