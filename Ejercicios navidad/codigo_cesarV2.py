#Version 2 del código (sólo con elementos que hemos visto en clases)
#En esta versión evité recorrer nuevamente el abecedario por cada rot que hacemos almacenando las posiciones de las letras en un array
#Y aplicando la rot solo a ese nuevo array

abecedario='abcdefghijklmnñopqrstuvwxyz'
decifrar = input('Ingrese el texto a decifrar en minusculas: ')
posiciones = []
rot=0

#Con esto de abajo obtenemos las posiciones en el abecedario de cada una de las letras
for letra in decifrar: 
    for posicion in range(len(abecedario)):  
        if letra == abecedario[posicion]:
            posiciones.append(posicion)

#Ahora solo tenemos que mostrar por pantalla el valor del abecedario en cada posicion y crear un ciclo para que imprima cada rotacion posible
while rot < len(abecedario):
    print('Intentando con rot', rot, ':', sep='')
    for posicion in posiciones:
        print(abecedario[(posicion+rot)%27], end='')
    print('\n', '-'*30, '\n')
    rot+=1
