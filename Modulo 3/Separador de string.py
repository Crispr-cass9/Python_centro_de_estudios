entrada = input("Ingrese su string a separar o -1 para finalizar: ")
subcadena=[]
lista_final=[]
while entrada != "-1":
    lista = entrada.split(sep=",")
    for elemento in lista:
        subcadena.append(elemento.split(sep="y"))

    for elemento in subcadena:
        for item in elemento:
            print(item)
            
    entrada = input("Ingrese su string a separar o -1 para finalizar: ")
    subcadena=[]
    lista_final=[]
    
    
