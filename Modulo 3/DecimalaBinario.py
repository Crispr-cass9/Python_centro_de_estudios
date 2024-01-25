#Programa que convierte un número decimal a binario


def decimal_a_binario(decimal,  string):
    if decimal !=0:
        division = str(decimal%2)
        string = division + string
        decimal_a_binario(decimal//2, string)
    else:
        print(str(string).zfill(8))

entrada = input("Ingrese el decimal a convertir: ")

while entrada != "salir":
    decimal_a_binario( int(entrada) , "")
    entrada = input("Ingrese salir o un nuevo número: ")

