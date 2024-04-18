class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


class Alumno(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def __str__(self):
        return super().__str__() + f", Grado: {self.grado}"

    def estudiar(self, asignatura):
        return f"{self.nombre} está estudiando {asignatura.nombre}"


class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def __str__(self):
        return super().__str__() + f", Especialidad: {self.especialidad}"

    def enseñar(self, asignatura):
        return f"{self.nombre} está enseñando {asignatura.nombre}"


class Asignatura:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

    def __str__(self):
        return f"Asignatura: {self.nombre}, Créditos: {self.creditos}"


class Aula:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad

    def __str__(self):
        return f"Aula {self.numero}, Capacidad: {self.capacidad}"


alumno1 = Alumno("Juan", 16, "10°")
profesor1 = Profesor("María", 35, "Matemáticas")
asignatura1 = Asignatura("Matemáticas Avanzadas", 5)
aula1 = Aula(101, 30)

print(alumno1)
print(profesor1)
print(asignatura1)
print(aula1)

print(alumno1.estudiar(asignatura1))
print(profesor1.enseñar(asignatura1))
