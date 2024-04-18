class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_pago(self):
        return self.salario

    def __str__(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}"


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def __str__(self):
        return f"Desarrollador: {self.nombre}, Salario: {self.salario}, Lenguaje: {self.lenguaje}"


class Gerente(Empleado):
    def __init__(self, nombre, salario, nivel):
        super().__init__(nombre, salario)
        self.nivel = nivel

    def calcular_pago(self):
        # Los gerentes reciben un bono adicional
        return super().calcular_pago() + 1000

    def __str__(self):
        return f"Gerente: {self.nombre}, Salario: {self.salario}, Nivel: {self.nivel}"


def menu():
    print("\nMenu:")
    print("1. Crear empleado")
    print("2. Mostrar empleados")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


empleados = []

while True:
    opcion = menu()

    if opcion == "1":
        tipo_empleado = input("¿Qué tipo de empleado desea crear? (Desarrollador/Gerente): ")
        nombre = input("Ingrese el nombre del empleado: ")
        salario = float(input("Ingrese el salario del empleado: "))

        if tipo_empleado.lower() == "desarrollador":
            lenguaje = input("Ingrese el lenguaje de programación del desarrollador: ")
            empleado = Desarrollador(nombre, salario, lenguaje)
        elif tipo_empleado.lower() == "gerente":
            nivel = input("Ingrese el nivel del gerente: ")
            empleado = Gerente(nombre, salario, nivel)
        else:
            print("Tipo de empleado no válido.")
            continue

        empleados.append(empleado)
        print("Empleado creado correctamente.")

    elif opcion == "2":
        if len(empleados) == 0:
            print("No hay empleados registrados.")
        else:
            print("Lista de empleados:")
            for empleado in empleados:
                print(empleado)

    elif opcion == "3":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
