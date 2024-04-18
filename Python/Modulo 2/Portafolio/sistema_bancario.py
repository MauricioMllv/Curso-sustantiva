class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuenta = None

    def asignar_cuenta(self, cuenta):
        self.cuenta = cuenta

    def __str__(self):
        return f"Cliente: {self.nombre}"


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad
        return f"Se depositaron {cantidad} unidades. Nuevo saldo: {self.saldo}"

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"Se retiraron {cantidad} unidades. Nuevo saldo: {self.saldo}"
        else:
            return "Fondos insuficientes"

    def obtener_saldo(self):
        return f"Saldo actual: {self.saldo}"

    def __str__(self):
        return f"Cuenta de {self.titular}: Saldo: {self.saldo}"


def menu():
    print("\nMenu:")
    print("1. Crear cliente")
    print("2. Crear cuenta bancaria")
    print("3. Depositar")
    print("4. Retirar")
    print("5. Ver saldo")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


clientes = []
cuentas = []

while True:
    opcion = menu()

    if opcion == "1":
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        cliente = Cliente(nombre_cliente)
        clientes.append(cliente)
        print("Cliente creado exitosamente.")

    elif opcion == "2":
        if len(clientes) == 0:
            print("Debe crear un cliente primero.")
        else:
            print("Clientes disponibles:")
            for i, cliente in enumerate(clientes):
                print(f"{i + 1}. {cliente.nombre}")
            cliente_index = int(input("Seleccione el cliente: ")) - 1
            saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
            cuenta = CuentaBancaria(clientes[cliente_index].nombre, saldo_inicial)
            clientes[cliente_index].asignar_cuenta(cuenta)
            cuentas.append(cuenta)
            print("Cuenta bancaria creada exitosamente.")

    elif opcion == "3":
        if len(cuentas) == 0:
            print("No hay cuentas bancarias creadas.")
        else:
            print("Cuentas bancarias disponibles:")
            for i, cuenta in enumerate(cuentas):
                print(f"{i + 1}. {cuenta.titular}")
            cuenta_index = int(input("Seleccione la cuenta: ")) - 1
            cantidad_deposito = float(input("Ingrese la cantidad a depositar: "))
            print(cuentas[cuenta_index].depositar(cantidad_deposito))

    elif opcion == "4":
        if len(cuentas) == 0:
            print("No hay cuentas bancarias creadas.")
        else:
            print("Cuentas bancarias disponibles:")
            for i, cuenta in enumerate(cuentas):
                print(f"{i + 1}. {cuenta.titular}")
            cuenta_index = int(input("Seleccione la cuenta: ")) - 1
            cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
            print(cuentas[cuenta_index].retirar(cantidad_retiro))

    elif opcion == "5":
        if len(cuentas) == 0:
            print("No hay cuentas bancarias creadas.")
        else:
            print("Cuentas bancarias disponibles:")
            for i, cuenta in enumerate(cuentas):
                print(f"{i + 1}. {cuenta.titular}")
            cuenta_index = int(input("Seleccione la cuenta: ")) - 1
            print(cuentas[cuenta_index].obtener_saldo())

    elif opcion == "6":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
