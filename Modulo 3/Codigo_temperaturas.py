import random

lista = [[round(random.uniform(-3, 39),2) for x in range(24)]for x in range(31)]

sobre_20 = [temperatura for dia in lista for temperatura in dia if temperatura>20]

promedio = sum([dia[11] for dia in lista])/31

mas_alta = 1

mas_baja = 1

print('-'*20, 'Promedio', '-'*20)
print(promedio)
print('-'*20, 'sobre 20', '-'*20)
print(sobre_20)
print('-'*20, 'Mas alta', '-'*20)
print(mas_alta)
print('-'*20, 'Mas baja', '-'*20)
print(mas_baja)