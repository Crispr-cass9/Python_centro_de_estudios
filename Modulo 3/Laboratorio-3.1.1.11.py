income = float(input("Introduce el ingreso anual:"))

if income<=85528:
    tax = income*.18-556.02
else:
    tax = 14839+(income-85528)*.32
tax = round(tax, 0)

if tax <= 0:
    tax = 0
    
print("El impuesto es:", tax, "pesos")
