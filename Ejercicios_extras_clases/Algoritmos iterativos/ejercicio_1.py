#Calcula el factorial de un número dado.

def factorial(n):
    if n<0:
        return 'Este cálculo no se puede realizar'
    if n <= 1:
        return 1
    total=1
    for i in range(1,n+1):
        total*=i
    return total

print(factorial(5))