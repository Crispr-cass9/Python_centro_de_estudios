'''
Dado a un array de char, el siguiente método escribe en la salida estándar los
sucesivos prefijos de a, de más corto a más largo.
Por ejemplo, si a = [ 'a', 'b', 'c', 'd', 'e' ], se escribe:
• a
• ab
• abc
• abcd
• abcde

'''

def ejercicio(lista):
    imprimir = ""
    for i in range(len(lista)):
        imprimir+=lista[i]
        print(imprimir)
    return 'Finalizado'
print(ejercicio([ 'a', 'b', 'c', 'd', 'e']))