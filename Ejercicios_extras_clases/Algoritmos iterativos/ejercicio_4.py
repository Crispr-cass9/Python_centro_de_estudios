def coincidencias(lista, buscar):
    return len([x for x in lista if x == buscar])

lista=[ 'g', 'g', 'a', 'c', 't', 'g', 'a ']

print(coincidencias(lista, 'g'))
