from random import randint


'''
Función: obtener_loteria()
Entrada: n/a
Salida: Una lista con los números de la loteria: [num1, num2, num3...num8] 
'''
def obtener_loteria():
    loteria = []
    i=0
    while i < 8:
        random_num = randint(1, 32)
        if random_num not in loteria:
            loteria.append(random_num)
        else:
            i-=1
        i+=1
    return loteria

'''
Función: crear_lista_jugadores()
Entrada: n/a
Salida: Una lista con forma [[nombre1], [nombre2], [nombre3]]
'''
def crear_lista_jugadores():
    jugadores = []
    nombres = [input("Ingrese el nombre de el o los jugadores: ")]
    while nombres != ["-1"]:
        jugadores.append(nombres)
        nombres = [input("Ingrese el nombre del siguiente jugador o -1 para continuar: ")]
    return jugadores

'''
Función: obtener_apuestas_jugadores(entrada)
Entrada: Una lista con forma [[nombre1], [nombre2], [nombre3]]
Salida: Una lista con forma [[Nombre1, [num1, num1, num3... num8]], [Nombre2, [num1, num1, num3... num8]]
'''
def obtener_apuestas_jugadores(lista_jugadores):
    

    for i in range(len(lista_jugadores)):
        j = 0
        números=[]
        while j <8:
            números.append(int(input(f"Turno de {lista_jugadores[i][0]} ingresa tus números {j+1}/8: ")))
            j+=1
        lista_jugadores[i].append(sorted(números))
    return lista_jugadores

'''
Función: obtener_apuestas_jugadores(entrada)
Entrada: Una lista con forma [[Nombre1, [num1, num1, num3... num8]], [Nombre2, [num1, num1, num3... num8]]
Salida: Sin salida, imprimesión en pantalla de resultados
'''
def comparar_resultado_loterias(jugadores_y_apuestas):
    loteria = obtener_loteria()
    for i in range(len(jugadores_y_apuestas)):
        aciertos = 0
        for elemento in loteria:
            if elemento in jugadores_y_apuestas[i][1]:
                aciertos +=1
        print(f"{jugadores_y_apuestas[i]}, ha obtenido {aciertos} aciertos")
    loteria= sorted(loteria)
    print("La loteria fue", loteria)

jugadores = crear_lista_jugadores()

apuestas = obtener_apuestas_jugadores(jugadores)                
            
resultados = comparar_resultado_loterias(apuestas)
