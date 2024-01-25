'''
El siguiente método calcula el número de cifras de a que valen d. Por ejemplo,
para a = 405659 y d = 5, el método devuelve 2.
'''
def cifras(n, buscar):
    cantidad=0
    if buscar > 9 or buscar<0:
        return 'La cifra a buscar debe ser positiva y menor que 9'
    while n != 0:
        if n%10==buscar:
            cantidad+=1
        n = n//10
    return cantidad
print(cifras(51255, 5))