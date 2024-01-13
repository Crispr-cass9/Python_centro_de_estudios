print("HUCHA MEJORADA'")

objetivo = float(input("¿Cuantos euros quiere ahorrar?: "))
dinero_total = 0 #Yo en la vida
añadir_a_hucha = 0

while objetivo < 0:
    objetivo = float(input("La meta de ahorro no puede ser inferior a cero, ingrese una nueva meta: "))

while dinero_total < objetivo:
    añadir_a_hucha = float(input("¿Cuántos euros quiere añadir a la hucha?: "))
    if añadir_a_hucha < 0:
        print("Por favor, ingrese una cantidad positiva")
        continue
    dinero_total += añadir_a_hucha
    
print("¡Objetivo conseguido!, Ha ahorrado usted", dinero_total, "euros")



