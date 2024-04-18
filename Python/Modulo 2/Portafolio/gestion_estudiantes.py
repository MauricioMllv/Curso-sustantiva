class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = []

    def agregar_calificaciones(self, cantidad):
        for _ in range(cantidad):
            calificacion = float(input("Ingrese la calificación: "))
            self.calificaciones.append(calificacion)

    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Calificaciones: {self.calificaciones}, Promedio: {self.calcular_promedio()}"

def menu():
    print("\nMenu:")
    print("1. Ingresar estudiante")
    print("2. Ver estudiantes")
    print("3. Agregar calificaciones")
    print("4. Ver todas las calificaciones de estudiantes")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

estudiantes = []

while True:
    opcion = menu()

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        estudiante = Estudiante(nombre, edad)
        estudiantes.append(estudiante)
        print("Estudiante ingresado correctamente.")

    elif opcion == "2":
        if len(estudiantes) == 0:
            print("No hay estudiantes ingresados.")
        else:
            print("Lista de estudiantes:")
            for estudiante in estudiantes:
                print(estudiante)

    elif opcion == "3":
        if len(estudiantes) == 0:
            print("No hay estudiantes ingresados.")
        else:
            print("Seleccione el estudiante:")
            for i, estudiante in enumerate(estudiantes):
                print(f"{i+1}. {estudiante.nombre}")
            seleccion = int(input()) - 1
            estudiante_seleccionado = estudiantes[seleccion]
            cantidad_calificaciones = int(input("Ingrese la cantidad de calificaciones que desea agregar: "))
            estudiante_seleccionado.agregar_calificaciones(cantidad_calificaciones)
            print("Calificaciones agregadas correctamente.")

    elif opcion == "4":
        if len(estudiantes) == 0:
            print("No hay estudiantes ingresados.")
        else:
            print("Todas las calificaciones de los estudiantes:")
            for estudiante in estudiantes:
                print(f"{estudiante.nombre}: {estudiante.calificaciones}")

    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
