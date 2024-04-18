def ingresar_notas():
    cantidad_notas = int(input("Ingrese la cantidad de notas: "))
    
    notas = []
    for i in range(cantidad_notas):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)
    
    return notas

def contar_notas_mayores_al_promedio(notas):
    promedio = sum(notas) / len(notas)
    contador = 0
    for nota in notas:
        if nota > promedio:
            contador += 1
    return contador

def main():
    notas = ingresar_notas()
    
    cantidad_mayores_al_promedio = contar_notas_mayores_al_promedio(notas)
    
    print(f"\nLa cantidad de notas mayores al promedio es: {cantidad_mayores_al_promedio}")

if __name__ == "__main__":
    main()
