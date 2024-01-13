print("COMPARADOR DE NÚMEROS")

primer_numero = float(input("Escriba un número: "))
segundo_numero = float(input("Escriba otro número: "))

if primer_numero > segundo_numero:
    print("Menor: ", segundo_numero, "; Mayor:", primer_numero, sep="")
elif primer_numero < segundo_numero:
    print("Menor: ", primer_numero, "; Mayor: ", segundo_numero, sep ="")
else:
    print("Los dos números son iguales.")
