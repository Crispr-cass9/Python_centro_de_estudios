print("PROGRAMA 'CONFIRME SU CONTRASEÑA'")

contraseña = input("Escriba su contraseña: ")
comprobar = input("Escriba nuevamente su contraseña: ")

while contraseña != comprobar:
    print("Las contraseñas no coinciden. Inténtelo de nuevo: ")
    contraseña = input("Escriba su contraseña: ")
    comprobar = input("Escriba nuevamente su contraseña: ")

print("Contraseña confirmada. ¡Hasta la vista!")


