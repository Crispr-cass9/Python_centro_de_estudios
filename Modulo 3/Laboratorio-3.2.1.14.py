blocks = int(input("Ingresa el número de bloques: "))
total_blocks = 0
height = 0
while total_blocks + height + 1 <= blocks:
    total_blocks += height + 1
    height +=1

print("La altura de la pirámide:", height)
