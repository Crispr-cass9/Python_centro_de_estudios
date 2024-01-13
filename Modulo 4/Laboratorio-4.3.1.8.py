def is_year_leap(year):
    if year % 4 != 0: #no divisible entre 4 no bisiesto
	    return False
    elif year % 4 == 0 and year % 100 != 0: #divisible entre 4 y no entre 100 o 400 Bisiesto
    	return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: #divisible entre 4 y 10 y no entre 400 No bisiesto
    	return False
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #divisible entre 4, 100 y 400 bisiesto
    	return True


def days_in_month(year, month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        months[1]=29
    return months[month-1]


def day_of_year(year, month, day):
    if (month == 2 and day == 29) and not is_year_leap(year):
        return "Error, el año seleccionado no es bisiesto por lo que no existe un 29 de febrero"
        
    if month <=2:
        year -= 1
        month += 12

    k = year%100
    j = year//100
    h = (day + (13*(month+1)//5) + k + (k//4) + (j//4) + 5*j)%7
    week = ['Sábado', 'Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
    return week[h]

print(day_of_year(2023, 10, 31))
