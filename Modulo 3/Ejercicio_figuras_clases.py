'''
Hacer formas con asteriscos:
1.- Cuadrado
2.- Triangulo
3.- Triangulo invertido
3.- Arbol de navidad
4.- Rombo

'''
pisos = int(input("introduzca el numero de pisos: "))

for i in range(pisos):
        print("*   "*pisos)

print()

for i in range(pisos):
    print("*   "*(i+1))

print()

for i in range(pisos):
    print("*   "*(pisos-i))

print()

for i in range(pisos):
        print("   "*(pisos+1-i)," * "*(1+2*i), sep = "")



for i in range(pisos):
        print("   "*(pisos+1-i)," * "*(1+2*i), sep = "")

for i in range(pisos-4):
        print("   "*(pisos-1),   " * "*((pisos//2)+1), sep = "")
        


            
            
        

