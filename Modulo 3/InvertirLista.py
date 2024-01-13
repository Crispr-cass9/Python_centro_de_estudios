lista= []
contador = 1
entrada = int(input(f"Ingrese el elemento: {contador} de la lista, utilize -1 para continuar: "))


while entrada != -1:
    lista.append(entrada)
    contador+=1
    entrada = int(input(f"Ingrese el elemento: {contador} de la lista, utilize -1 para continuar: "))
    

for i in range(len(lista)//2):
    lista[i], lista[len(lista)-1-i] = lista[len(lista)-1-i], lista[i]

for i in range(len(lista)-1):
    print(lista[i], end=", ")
print(lista[len(lista)-1])
