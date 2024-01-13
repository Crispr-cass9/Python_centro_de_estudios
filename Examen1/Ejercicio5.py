print("DIVISOR DE NÚMEROS")

dividendo = int(input("Escriba el dividendo: "))
divisor = int(input("Escriba el divisor: "))

if divisor == 0:
    print("No se puede dividir por cero.")
elif dividendo%divisor != 0:
    print("La división no es exacta. Cociente:", dividendo//divisor, "Resto:", dividendo%divisor)
else:
    print("La división es exacta. Cociente:", dividendo//divisor)
