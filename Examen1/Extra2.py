print("PROGRAMA 'CONFIRME SU CONTRASEÑA'")

contraseña = input("Escriba su contraseña: ")
print("Tiene 3 intentos para confirmar su contraseña")
comprobar = input("Escriba nuevamente su contraseña: ")
contador_errores=0

while contraseña != comprobar:   
    contador_errores+=1
    if contador_errores == 3:
        break
    print("Las contraseñas no coinciden (Intento ", contador_errores+1, "de 3)")
    comprobar = input("Escriba nuevamente su contraseña: ")


if contador_errores==3:
    print("Lo siento, no ha confirmado la contraseña, ¡Hasta la vista!")  
else: print("Contraseña confirmada. ¡Hasta la vista!")


