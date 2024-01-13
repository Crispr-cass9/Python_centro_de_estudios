#Programa que recibe el peso (Kg) y altura (m) de una persona y calcula su imc

print("Cálculo del índice de masa corporal")

peso = float(input("¿Cuánto pesa? "))
altura = float(input("Cuánto mide en metros? "))

print ("Su imc es", round(peso/altura**2, 1), """\nUn imc muy alto indica obesidad. Los valores normales de imc están entre 20 y 25,
pero esos límites dependen de la edad, sexo, de la constitución física, etc""")

