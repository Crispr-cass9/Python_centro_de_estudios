'''
Dado a un array de char, y un carácter c, el siguiente método comprueba si c
aparece repetido en a. Por ejemplo, si a es [ 'g', 'g', 'a', 'c' ,'t' ,'a' ,'g' ,'a' ], y c
es 'a' el método devuelve true. Para el mismo array, si c es 't' el método
devuelve false
'''
lista =[ 'g', 'g', 'a', 'c' ,'t' ,'a' ,'g' ,'a' ]

def comprobar(lista, buscar):
    if buscar == 'a':
        return 1 < len([x for x in lista if x == buscar])    
    else:
        return 1 < len([x for x in lista if x == buscar])


print(comprobar(lista, 't'))