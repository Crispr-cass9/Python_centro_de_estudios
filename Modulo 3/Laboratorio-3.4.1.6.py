hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

hat_list[2] = int(input("Ingrese el nuevo número: "))

del hat_list[4]

print(hat_list, "Longitud:", len(hat_list))
