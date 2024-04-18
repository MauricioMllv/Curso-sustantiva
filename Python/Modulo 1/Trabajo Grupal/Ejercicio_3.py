def info_mes(mes):
    meses_info = [
        ("Enero", 31),
        ("Febrero", 28),
        ("Marzo", 31),
        ("Abril", 30),
        ("Mayo", 31),
        ("Junio", 30),
        ("Julio", 31),
        ("Agosto", 31),
        ("Septiembre", 30),
        ("Octubre", 31),
        ("Noviembre", 30),
        ("Diciembre", 31)
    ]

    if 1 <= mes <= 12:
        nombre_mes, dias = meses_info[mes - 1]
        print(f"{nombre_mes} tiene {dias} días.")
    else:
        print("Número de mes no válido. Debe ingresar entre 1 y 12.")

numero_mes = int(input("Ingrese un número de mes (1 al 12): "))
info_mes(numero_mes)
