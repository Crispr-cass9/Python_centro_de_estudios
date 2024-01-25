'''
Dado a un array de int, los siguientes métodos devuelven un array del mismo
tamaño que a, tal que la componente i del resultado contiene la suma de las
componentes en a[0 ... i].
Por ejemplo, si a = [ 1, 4, 2, -1, 0, 3 ], devuelven el array [ 1, 5, 7, 6, 6, 9 ].
'''

def ejercicio(lista):
    
    devolver=[]
    devolver.append(lista[0])

    for i in range(1,len(lista)):
        devolver.append(devolver[-1]+lista[i])
    return devolver

print(ejercicio([ 1, 4, 2, -1, 0, 3 ]))