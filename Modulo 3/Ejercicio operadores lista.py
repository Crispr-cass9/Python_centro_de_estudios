large = int(input("¿Cuántos elementos quiere agregar a la lista?: "))
lista= []

for i in range(large):
    lista.append(int(input(f"Ingrese el elemento número {i+1}: ")))

print("Su lista actual es", lista)

operación = int(input("0 Para Suma, 1 es para Resta, 2 es Para multiplicación, 3 es para división,  4 es para exponenciación: "))

if operación == 0:
    cantidad = int(input("¿Qué cantidad le quiere sumar a cada elemento?: "))
    i=0
    for element in lista:
        lista[i] = element+cantidad
        i+=1

elif operación == 1:
    cantidad = int(input("¿Qué cantidad le quiere restar a cada elemento?: "))
    i=0
    for element in lista:
        lista[i] = element-cantidad
        i+=1

elif operación == 2:
    cantidad = int(input("¿Por qué cantidad quiere multiplicar cada elemento?: "))
    i=0
    for element in lista:
        lista[i] = element*cantidad
        i+=1

elif operación == 3:
    cantidad = int(input("¿Por qué cantidad quiere dividir cada elemento?: "))
    i=0
    for element in lista:
        lista[i] = element/cantidad
        i+=1


elif operación == 4:
    cantidad = int(input("¿Por qué cantidad quiere exponenciar cada elemento?: "))
    i=0
    for element in lista:
        lista[i] = element ** cantidad
        i+=1

print(lista)
