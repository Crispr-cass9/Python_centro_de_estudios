'''
Anotaciones de Cris, programé esto a las 2 am con sueño, en ese entonces solo 2 personas sabíamos lo que hacía este código, Dios y yo,
actualmente solo dios sabe como funciona, te deseo suerte tratando de comprenderlo

PD: la version 2 y 3 son mucho más entendibles que esto
'''

def buscar_ubicacion(msg, alf):
    ubicaciones=[]
    for elemento in msg:
        if elemento == ' ':
                ubicaciones.append(None)
                continue
        for posicion in range(len(alf)):     
            if elemento == alf[posicion]:
                ubicaciones.append(posicion)
    return ubicaciones

def codVig(msg, alf, clave):
    ubicaciones_clave = buscar_ubicacion(clave, alf)
    ubicaciones_msg = buscar_ubicacion(msg, alf)
    cifrado = ''
    indice=0

    for contador in range(len(ubicaciones_msg)):

        if ubicaciones_msg[contador] is None:
            cifrado+=' '
            continue

        cifrado+=alf[(ubicaciones_msg[contador] + ubicaciones_clave[indice%len(ubicaciones_clave)])%len(alf)]
        indice+=1
    return cifrado
     

print(codVig('atacar al anochecer' ,'abcdefghijklmnñopqrstuvwxyz', 'limon'))


