""" 
Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla.
"""

paises = []

for x in range(5):
    nombre = input("Ingrese el nombre del pais: ")
    paises.append(nombre)

print(f"Lista de paises\n{paises}")

for y in range(4):
    for z in range(4):
        if paises[z] > paises[z+1]:
            aux = paises[z]
            paises[z] = paises[z+1]
            paises[z+1] = aux

print(f"Lista ordenada alfabeticamente\n{paises}")