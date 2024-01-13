abecedario='abcdefghijklmnñopqrstuvwxyz' #Utilizamos un string que contiene el abecedario completo para buscar la posicion de las letras
decifrar = input('Ingrese el texto a decifrar en minusculas: ')
clave=0 #Esta variable almacena la rotación que se está utilizando en ese momento
while True: 

    if clave == 27: #Como nuestro abecedario posee 27 letras hay 27 posibles rotaciones
        break # una vez que complete todas las rotaciones posibles saldrá del bucle

    print('Intentando con ROT', clave, ':', sep='') 

#Antes de entrar a la zona de los bucles es necesario entender que la clave que utilizamos va aumentando progresivamente, esto quiere decir que
#cada vez que se decifra todo el mensaje con el primer intento de clave esta se aumenta en 1 

#Ahora, por cada letra en el texto a decifrar recorreremos todo el abecedario y buscaremos las posiciones en las que la letra del abecedario
#Sea igual a la letra que buscamos del mensaje a decifrar
#A esta posicion le sumamos el valor de la clave actual para que se realicen todas las posibilidades de rotación que existen
    for letra in decifrar: 
        for posicion in range(len(abecedario)):  
            if letra == abecedario[posicion]:
                print(abecedario[(posicion+clave)%27], end='')

    print('\n'+'-'*30) #Esto es estético para que las salidas por terminal se vean más claras
    clave+=1

#DESVENTAJAS DE MI PRIMERA SOLUCIÓN
#1.- Recorremos de forma innecesaria el abecedario por cada una de las rotaciones, cuando en realidad solo basta con obtener las posiciones iniciales una vez
#2.- A mi parecer el código es poco entendible
