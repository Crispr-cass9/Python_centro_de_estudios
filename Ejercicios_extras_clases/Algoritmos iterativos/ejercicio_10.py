'''
Sea a un array de int, cuyas componentes están todas iniciadas a 0. El
siguiente método asigna valores de la sucesión 1, 2, 3, ... al inicio de subarrays
de a cada vez más pequeños, de tamaño mitad.
Por ejemplo, si a es
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], se cambia a
[ 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 3, 0, 4 ].
'''

def ejercicio(lista):
    contador = 0
    inicio = 0
    while len(lista[inicio:]):
        contador+=1
        lista[inicio] = contador
        if len(lista[inicio:])%2  == 0:
            inicio += len(lista[inicio:])//2
        else:
            inicio += len(lista[inicio:])//2+1
    return lista





        

        
print(ejercicio([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]))