class AgendaContactos:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono
        print(f"Contacto {nombre} agregado correctamente.")

    def ver_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("Lista de contactos:")
            for nombre, telefono in self.contactos.items():
                print(f"{nombre}: {telefono}")

    def buscar_contacto(self, nombre):
        if nombre in self.contactos:
            print(f"Nombre: {nombre}, Teléfono: {self.contactos[nombre]}")
        else:
            print(f"El contacto {nombre} no se encuentra en la agenda.")

def main():
    agenda = AgendaContactos()

    while True:
        print("\nMenu:")
        print("1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Buscar contacto")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            agenda.agregar_contacto(nombre, telefono)
        elif opcion == '2':
            agenda.ver_contactos()
        elif opcion == '3':
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            agenda.buscar_contacto(nombre)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción correcta.")

if __name__ == "__main__":
    main()
