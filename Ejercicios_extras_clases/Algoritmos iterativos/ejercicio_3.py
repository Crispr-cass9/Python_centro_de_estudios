'''
Dados dos enteros positivos a y b, tales que a >= b, el siguiente método
calcula el número de cifras de b que aparecen como terminación de a.Es decir,
calcula cuántas cifras consecutivas de b coinciden con consecutivas cifras de
a, leyendo las cifras de derecha a izquierda.
Por ejemplo si a es 8714509867 y b es 9467, el método devuelve 2, dado que
las dos últimas cifras de a coinciden con las de b.
'''

def coinciden(cifra1, cifra2):
    
    cantidad = 0

    while cifra2 != 0: 
        
        if cifra1%10 == cifra2%10:
            cantidad+=1
    
        else: 
            return cantidad
    
        cifra1=cifra1//10
        cifra2=cifra2//10

    return cantidad

print(coinciden(8714509867, 9467))
    