"""
Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más caracteres.
"""

lista = ["Ana", "Deylan", "Edmmee", "Astrid", "Juan"]

total = 0

for x in range(len(lista)):
    if len(lista[x]) >= 5:
        total += 1

print(f"El total de nombres que tienen 5 o mas caracteres son: {total}")