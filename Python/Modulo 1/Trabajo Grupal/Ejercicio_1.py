def imprimir_numeros(numero):
    if numero <= 0 or numero > 100:
        print("Número no válido. Por favor, ingrese un número del 1 al 100.")
        return

    if numero % 2 == 0:
        print(f"Números pares siguientes al {numero}:")
        for i in range(numero + 2, 101, 2):
            print(i)
    else:
        print(f"Números impares siguientes al {numero}:")
        for i in range(numero + 2, 100, 2):
            print(i)

while True:
    try:
        numero_ingresado = int(input("Ingrese un número del 1 al 100 (o ingrese 0 para salir): "))

        imprimir_numeros(numero_ingresado)
    except ValueError:
        print("Por favor, ingrese un número válido.")
