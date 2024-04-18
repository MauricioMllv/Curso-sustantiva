class Pelicula:
    def __init__(self, titulo, director, genero, duracion):
        self.titulo = titulo
        self.director = director
        self.genero = genero
        self.duracion = duracion

    def obtener_informacion(self):
        return f"Título: {self.titulo}, Director: {self.director}, Género: {self.genero}, Duración: {self.duracion} minutos"


class Estreno(Pelicula):
    def __init__(self, titulo, director, genero, duracion, fecha_estreno):
        super().__init__(titulo, director, genero, duracion)
        self.fecha_estreno = fecha_estreno

    def obtener_informacion(self):
        return super().obtener_informacion() + f", Fecha de estreno: {self.fecha_estreno}"


def agregar_pelicula():
    titulo = input("Ingrese el título de la película: ")
    director = input("Ingrese el director de la película: ")
    genero = input("Ingrese el género de la película: ")
    duracion = int(input("Ingrese la duración de la película (en minutos): "))
    return Pelicula(titulo, director, genero, duracion)



def agregar_estreno():
    titulo = input("Ingrese el título del estreno: ")
    director = input("Ingrese el director del estreno: ")
    genero = input("Ingrese el género del estreno: ")
    duracion = int(input("Ingrese la duración del estreno (en minutos): "))
    fecha_estreno = input("Ingrese la fecha de estreno del estreno: ")
    return Estreno(titulo, director, genero, duracion, fecha_estreno)


def mostrar_peliculas(peliculas):
    print("\n=== Películas ===")
    for i, pelicula in enumerate(peliculas):
        print(f"\nPelícula {i + 1}:")
        print(pelicula.obtener_informacion())



peliculas = []


for _ in range(5):
    print("\nIngrese los detalles de la nueva película o estreno:")
    tipo_estreno = input("¿Es un estreno? (si/no): ").lower()
    if tipo_estreno == "si":
        pelicula = agregar_estreno()
    elif tipo_estreno == "no":
        pelicula = agregar_pelicula()
    else:
        print("Opción no válida. Intente de nuevo.")
        continue
    peliculas.append(pelicula)


mostrar_peliculas(peliculas)
