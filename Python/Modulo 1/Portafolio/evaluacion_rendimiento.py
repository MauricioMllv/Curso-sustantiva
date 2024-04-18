def calcular_promedio(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

def evaluar_rendimiento(promedio):
    if promedio >= 4.0:
        return "Aprobado"
    else:
        return "Reprobado"

def main():
    cantidad_notas = int(input("Ingrese la cantidad de calificaciones: "))
    calificaciones = []
    for i in range(cantidad_notas):
        nota = float(input(f"Ingrese la calificación {i + 1}: "))
        calificaciones.append(nota)

    promedio = calcular_promedio(calificaciones)

    resultado = evaluar_rendimiento(promedio)

    print(f"El promedio del estudiante es: {promedio}")
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
