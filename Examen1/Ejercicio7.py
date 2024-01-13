print("COMPARADOR DE AÑOS")

anyo_actual = int(input("¿En qué año estamos?: "))
anyo_cualquiera = int(input("Escriba un año cualquiera: "))

if anyo_actual < anyo_cualquiera:
    print("Para llegar al año", anyo_cualquiera, "faltan", anyo_cualquiera-anyo_actual, "años")
elif anyo_actual > anyo_cualquiera:
    print("Desde el año", anyo_cualquiera, "han pasado", anyo_actual-anyo_cualquiera, "años")
else:
    print("¡Son el mismo año!")
