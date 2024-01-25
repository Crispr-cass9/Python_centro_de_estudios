'''
Dado a un array de char, el siguiente método escribe en la salida estándar los
sucesivos prefijos de a, de más corto a más largo, tales que el primer y último
carácter coinciden. Por ejemplo, si a = ['a', 'l', 'a', 'm', 'e', 'd', 'a' ], se escribe:
• a
• ala
• alameda
'''

def ejercicio(lista, letra):
    for i in range(len(lista)):
        concatenar = ""
        for x in lista[:i+1]:
            concatenar += x

        if concatenar[0] == concatenar[i]:
            print(concatenar)
    return 'finalizado'
print(ejercicio(['a', 'l', 'a', 'm', 'e', 'd', 'a', 'l', 'l', 'a' ], 'a'))