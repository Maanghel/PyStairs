"""
Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100.
"""

lista = [1, 2, 450, 4, 5, 320, 7, 8]

total = 0

for x in range(len(lista)):
    if lista[x] > 100:
        total += 1

print(f"El total de valores en la lista que son superiores a 100: {total}")