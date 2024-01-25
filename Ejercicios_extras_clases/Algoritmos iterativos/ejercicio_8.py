'''
Dado a un array de char y un char c, el siguiente método escribe en la salida
estándar los sucesivos prefijos de a, de más corto a más largo, que no
contienen el carácter c.
Por ejemplo, si a = [ 'e', 'j', 'e', 'm', 'p', 'l', 'o' ] y c es 'm', se escribe:
• e
• ej
• eje
'''
def ejercicio(lista, caracter):
    imprimir=''
    for i in range(len(lista)):
        
        if lista[i] == caracter:
            break
        imprimir+=lista[i]
        print(imprimir)
              
    return 'Finalizado'

print(ejercicio([ 'e', 'j', 'e', 'm', 'p', 'l', 'o' ], 'm'))