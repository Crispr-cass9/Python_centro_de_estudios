# Ordenamiento burbuja
lista = [10, 8, 6, 2, 4, 1]
j=0
while j < len(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    j+=1

print(lista)
            
#ordenamiento burbuja inverso

lista = [10, 8, 6, 2, 4, 1]
j=0
while j < len(lista):
    for i in range(len(lista)-1):
        if lista[i] < lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    j+=1

print(lista)
            
