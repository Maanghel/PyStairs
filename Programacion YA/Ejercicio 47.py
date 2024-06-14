""" 
Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra.
Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.
"""

productos = []
precios = []

for x in range(5):
    nom = input("Introduzca el nombre del producto: ")
    productos.append(nom)
    pre = float(input("Introduzca el precio del producto: "))
    precios.append(pre)

total_mayor = 0

for y in range(1,5):
    if precios[y] > precios[0]:
        total_mayor += 1

print("Lista de productos\tLista de precios")
for z in range(5):
    print(f"\t{productos[z]}\t\t\t{precios[z]}")

print(f"El total de productos que tienen un precio mayor al primero son de {total_mayor}")