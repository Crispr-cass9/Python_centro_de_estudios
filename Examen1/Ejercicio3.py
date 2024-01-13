print("CONVERTIDOR DE SEGUNDOS A MINUTOS")

segundos_a_convertir = int(input("Escriba la cantidad de segundos: "))

minutos_convertidos = segundos_a_convertir//60
segundos_restantes = segundos_a_convertir%60

if segundos_a_convertir == 1:
    print(segundos_a_convertir, "segundo es", minutos_convertidos, "minutos y", segundos_restantes, "segundo.")
          
elif minutos_convertidos ==1:
    print(segundos_a_convertir, "segundos son", minutos_convertidos, "minuto y ", end="")
    if segundos_restantes == 1:
        print(segundos_restantes, "segundo")
    else:
        print(segundos_restantes, "segundos")
else:
    print(segundos_a_convertir, "segundos son", minutos_convertidos, "minutos y ", end="")
    if segundos_restantes == 1:
        print(segundos_restantes, "segundo")
    else:
        print(segundos_restantes, "segundos")

