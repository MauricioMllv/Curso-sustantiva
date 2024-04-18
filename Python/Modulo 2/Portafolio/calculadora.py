def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def menu():
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def calculadora():
    while True:
        try:
            menu()
            opcion = int(input("Seleccione una operación (1-5): "))
            if opcion == 5:
                print("Saliendo de la calculadora.")
                break
            elif opcion < 1 or opcion > 5:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                continue

            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == 1:
                resultado = suma(num1, num2)
            elif opcion == 2:
                resultado = resta(num1, num2)
            elif opcion == 3:
                resultado = multiplicacion(num1, num2)
            elif opcion == 4:
                resultado = division(num1, num2)

            print("El resultado es:", resultado)

        except ValueError as e:
            print("Error:", e)
        except ZeroDivisionError as e:
            print("Error:", e)

calculadora()
