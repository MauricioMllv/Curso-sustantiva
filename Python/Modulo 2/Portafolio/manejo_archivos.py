def calcular_promedio(notas):
    total = sum(notas)
    return total / len(notas)

def leer_notas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            notas = [float(linea.strip().split()[1]) for linea in lineas]
        return notas
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return None
    except ValueError:
        print("El archivo contiene datos no numéricos.")
        return None

def escribir_promedio(promedio, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f"El promedio de las notas es: {promedio}")

def main():
    nombre_archivo_entrada = "registro_notas.txt"
    nombre_archivo_salida = "promedio_notas.txt"

    notas = leer_notas(nombre_archivo_entrada)

    if notas:
        promedio = calcular_promedio(notas)
        escribir_promedio(promedio, nombre_archivo_salida)
        print(f"Se ha calculado el promedio de las notas y se ha guardado en '{nombre_archivo_salida}'.")

if __name__ == "__main__":
    main()
