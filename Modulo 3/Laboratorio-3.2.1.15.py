c0 = int(input("Ingrese un número mayor a 0: "))

steps = 0

while c0 != 1:
    
    if c0%2 == 0:
        c0 /=2
        print(c0)
        steps+=1
    else:
        c0 = 3 * c0 + 1
        print(c0)
        steps+=1
        
print("Cantidad de pasos", steps)
