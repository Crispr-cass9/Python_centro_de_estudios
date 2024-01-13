Beatles = []

print("Paso 1:", Beatles)

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")

print("Paso 2:", Beatles)

for i in range(2):
    Beatles.append(input("Ingrese a Stu Sutcliffe y luego a Pete Best: "))
print("Paso 3:", Beatles)

del Beatles[3:5]
print("Paso 4:", Beatles)

Beatles.insert(0, "Ringo Star")
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))

