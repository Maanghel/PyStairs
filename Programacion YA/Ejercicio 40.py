"""
Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.
"""

lista = [3, 10, 25, 7, 5]

total = 0

for x in range(len(lista)):
    if lista[x] >= 7:
        total += 1

print(f"El total de valores de la lista que son mayores o iguales a 7: {total}")