""" 
Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista 
(es decir si dicho valor se encuentra en 2 o más posiciones en la lista)
"""

lista = []

for x in range (5):
    valor = int(input("Introduzca un entero: "))
    lista.append(valor)

mayor = lista[0]
repetidos = 0

for y in range(1,5):
    if lista[y] > mayor:
        mayor = lista[y]
    
    if y == 4:
        for z in range (5):
            if lista[z] == mayor:
                repetidos += 1

print(f"Lista de enteros:\n{lista}")
print(f"El mayor de esos enteros es {mayor} y se repite {repetidos} veces.")
