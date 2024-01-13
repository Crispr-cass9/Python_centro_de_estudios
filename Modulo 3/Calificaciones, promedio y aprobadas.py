asignaturas = [['Matemáticas'], ['Física'], ['Química'], ['Historia'], ['Lengua']]


for i in range(len(asignaturas)):
    notas = input(f"Ingrese las calificaciones que ha obtenido en {asignaturas[i][0]} separadas por un espacio: ")
    notas = notas.split(sep=" ")
    notas = [float(elemento) for elemento in notas]
    asignaturas[i].append(notas)

print('-------------------------------------------------------')

for i in range(len(asignaturas)):
    print('Las notas obtenidas en', asignaturas[i][0], 'son',  asignaturas[i][1])

print('-------------------------------------------------------')

for i in range(len(asignaturas)):
    print('El promedio final de', asignaturas[i][0], 'es', sum(asignaturas[i][1])/len(asignaturas[i][1]))

print('-------------------------------------------------------')

for i in range(len(asignaturas)):
    if sum(asignaturas[i][1])/len(asignaturas[i][1]) < 5:
        print('Debes recursar', asignaturas[i][0]) 
