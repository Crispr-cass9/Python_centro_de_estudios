'''
Digo lo mismo que en el ejercicio de cifrado con vigenere version 1, esto fue programado con sueño
'''

def decVig(msg, alf, clave):
    ubicaciones_clave = [alf.find(x) if x != ' ' else None for x in clave]
    ubicaciones_msg = [alf.find(x) if x != ' ' else None for x in msg]
    decifrado = ''
    indice=0

    for contador in range(len(ubicaciones_msg)):
        
        if ubicaciones_msg[contador] is None:
            decifrado+=' '
            continue        

        elif  ubicaciones_msg[contador] - ubicaciones_clave[indice%len(ubicaciones_clave)] >=0:
            decifrado+=alf[(ubicaciones_msg[contador] - ubicaciones_clave[indice%len(ubicaciones_clave)])%len(alf)]

        else:
            decifrado+=alf[(ubicaciones_msg[contador] - ubicaciones_clave[indice%len(ubicaciones_clave)] + len(alf))%len(alf)]
        indice+=1
    return decifrado

print(decVig('lbmqnc iw ozzkssooz', 'abcdefghijklmnñopqrstuvwxyz', 'limon'))