class Vehiculo:
    def __init__(self, color, marca, modelo, num_puertas, placa):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.num_puertas = num_puertas
        self.placa = placa

    def obtener_informacion(self):
        return f"Color: {self.color}, Marca: {self.marca}, Modelo: {self.modelo}, Número de puertas: {self.num_puertas}, Placa: {self.placa}"


class Automovil(Vehiculo):
    def __init__(self, color, marca, modelo, num_puertas, placa):
        super().__init__(color, marca, modelo, num_puertas, placa)


def agregar_automovil():
    color = input("Ingrese el color del automóvil: ")
    marca = input("Ingrese la marca del automóvil: ")
    modelo = input("Ingrese el modelo del automóvil: ")
    num_puertas = int(input("Ingrese el número de puertas del automóvil: "))
    placa = input("Ingrese la placa del automóvil: ")
    return Automovil(color, marca, modelo, num_puertas, placa)


def mostrar_automoviles(automoviles):
    print("\n=== Automóviles en el inventario ===")
    for i, automovil in enumerate(automoviles):
        print(f"\nAutomóvil {i + 1}:")
        print(automovil.obtener_informacion())

automoviles = []

for _ in range(5):
    print("\nIngrese los detalles del nuevo automóvil:")
    automovil = agregar_automovil()
    automoviles.append(automovil)

mostrar_automoviles(automoviles)
