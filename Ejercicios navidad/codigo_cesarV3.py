#Version 3 utilizando cosas sin limitaciones

abecedario='abcdefghijklmnñopqrstuvwxyz'
decifrar = input('Ingrese el texto a decifrar en minusculas: ')
posiciones = [[abecedario.index(letra)+rot for letra in decifrar] for rot in range(27)] #Es hermoso
indice=0

for rot in posiciones:
    mostrar=''
    for posicion in rot:
        mostrar+=abecedario[posicion%27]
    print('utilizando rot', indice, ' -----> ', mostrar, sep='', end='\n\n')
    indice+=1
    