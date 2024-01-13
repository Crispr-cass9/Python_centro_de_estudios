def codVig(msg, alf, clave):
    ubicaciones_msg = [alf.find(x) if x != ' ' else None for x in msg]
    ubicaciones_clave = [alf.find(x) if x != ' ' else None for x in clave]
    cifrado = ''
    indice=0
    for contador in range(len(ubicaciones_msg)):
        if ubicaciones_msg[contador] is None:
            cifrado+=' '
            continue
        cifrado+=alf[(ubicaciones_msg[contador] + ubicaciones_clave[indice%len(ubicaciones_clave)])%len(alf)]
        indice+=1
    return cifrado

print(codVig('atacar al anochecer', 'abcdefghijklmnñopqrstuvwxyz', 'limon'))