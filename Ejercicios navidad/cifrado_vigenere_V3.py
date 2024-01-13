def codVig(msg, alf, clave):
    cifrado = ''
    indice = 0

    for letra in msg:
        if letra == ' ':
            cifrado += ' '
            continue
        cifrado += alf[(alf.find(letra) + alf.find(clave[indice % len(clave)])) % len(alf)]
        indice += 1

    return cifrado

print(codVig('atacar al anochecer', 'abcdefghijklmnñopqrstuvwxyz', 'limon'))
