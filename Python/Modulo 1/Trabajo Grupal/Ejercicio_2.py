dic ={"Primera nota": 1 , "Segunda nota": 2 , "Tercera nota": 3 , "Cuarta nota": 4 , "Quinta nota": 5}
lista_notas=[]
for notas in dic.keys():
  while True:
    try:
      nota = int(input(f"ingrese la {notas}: "))
      if nota < 0 or nota > 10:
        print("Ingresar nota entre 0 y 10")
      else:
        lista_notas.append(nota)
        dic.update({notas: nota})
        break
    except ValueError:
      print("Ingrese un valor numérico")

promedio= sum(lista_notas)/len(lista_notas)

print("Las notas ingresadas son: ")
print(dic)

print("Nota minima es ",min(lista_notas))
print("Nota maxima es ",max(lista_notas))
print("Promedio de notas es: ",promedio)