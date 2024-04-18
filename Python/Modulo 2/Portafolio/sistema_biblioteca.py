class Autor:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print("El libro ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print("El libro no estaba prestado.")

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} - ISBN: {self.isbn} (Prestado: {'Sí' if self.prestado else 'No'})"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca no tiene libros.")
        else:
            print("Lista de libros en la biblioteca:")
            for libro in self.libros:
                print(libro)


def menu():
    print("\nMenu:")
    print("1. Agregar libro")
    print("2. Mostrar libros en la biblioteca")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


biblioteca = Biblioteca()

while True:
    opcion = menu()

    if opcion == "1":
        titulo = input("Ingrese el título del libro: ")
        autor_nombre = input("Ingrese el nombre del autor: ")
        autor = Autor(autor_nombre)
        isbn = input("Ingrese el ISBN del libro: ")
        libro = Libro(titulo, autor, isbn)
        biblioteca.agregar_libro(libro)
        print("Libro agregado correctamente.")

    elif opcion == "2":
        biblioteca.mostrar_libros()

    elif opcion == "3":
        if not biblioteca.libros:
            print("No hay libros en la biblioteca.")
        else:
            titulo_libro = input("Ingrese el título del libro que desea prestar: ")
            for libro in biblioteca.libros:
                if libro.titulo == titulo_libro:
                    libro.prestar()
                    break
            else:
                print("El libro no está en la biblioteca.")

    elif opcion == "4":
        if not biblioteca.libros:
            print("No hay libros en la biblioteca.")
        else:
            titulo_libro = input("Ingrese el título del libro que desea devolver: ")
            for libro in biblioteca.libros:
                if libro.titulo == titulo_libro:
                    libro.devolver()
                    break
            else:
                print("El libro no está en la biblioteca.")

    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
