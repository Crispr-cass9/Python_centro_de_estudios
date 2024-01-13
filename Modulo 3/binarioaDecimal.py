#Programa que toma un string en binario y lo convierte a decimal

while True:
    binario = input("Ingrese su numero binario: ")
    if binario == "salir":
        break
    binario = binario[::-1]
    total = 0
    for i in range(len(binario)):
           if binario[i] == "1":
               total += 2**i
    print(total)
        
                   
               
