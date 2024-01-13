lista_usuario = []
entrada= int(input('Ingrese los valores de su loteria, presione -1 para continuar'))

while entrada != -1:    
    lista_usuario.append(entrada)
    entrada= int(input('Ingrese los valores de su loteria, presione -1 para continuar'))
    


def ordenar_lista(lista):
    lista_ordenada=[]
    i=len(lista)-1
    j=len(lista)-1
    posicion=0

    
    while i >= 0:

        if len(lista) == 1:
            lista_ordenada.insert(0, lista[0])
            break
        mayor = lista[0]

        while j >= 0:
            if mayor < lista[j]:
                mayor = lista[j]
                posicion=j
            j-=1

            
        lista_ordenada.insert(0, lista[posicion])
        lista[0], lista[posicion] = lista[posicion], lista[0]
        del lista[0]
        j=len(lista)-1
        i-=1
        posicion = 0

        
    return lista_ordenada

print(ordenar_lista(lista_usuario))
