""" 
Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y mostrarla por pantalla, 
luego ordenar de mayor a menor e imprimir nuevamente.
"""

lista = []

for x in range(5):
    valor = int(input("Ingrese un numero entero: "))
    lista.append(valor)

for y in range(4):
    for z in range(4 - y):
        if lista[z] > lista[z+1]:
            aux = lista[z]
            lista[z] = lista[z+1]
            lista[z+1] = aux

print(f"Lista de numeros ordenada de menor a mayor\n{lista}")

for y in range(4):
    for z in range(4 - y):
        if lista[z] < lista[z+1]:
            aux = lista[z]
            lista[z] = lista[z+1]
            lista[z+1] = aux

print(f"Lista de numeros ordenada de mayor a menor\n{lista}")