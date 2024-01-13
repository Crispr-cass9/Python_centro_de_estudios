year = int(input("Introduce un año:"))

if (year > 1582):
    
    if year%4 != 0:
        print("Es un año común")
    elif year%100 !=0:
        print("Es un año bisiesto")
    elif year%400 !=0:
        print("Es un año común")
    else:
        print("Es un año bisiesto")
else:
    print("No dentro del periodo del calendario gregoriano")