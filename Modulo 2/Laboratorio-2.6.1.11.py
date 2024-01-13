hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

hour = (hour + dura//60 + (mins+ dura%60)//60)%24
mins = (mins + dura%60)%60



print(hour, ":", mins, sep = "");
