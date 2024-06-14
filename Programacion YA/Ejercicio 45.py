""" 
Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el nombre de persona menor en orden alfabético.
"""

lista = []

for x in range(5):
    nombre = input("Introduzca el nombre de la persona: ")
    lista.append(nombre)

menor = lista[0]

for y in range(1,5):
    if lista[y] < menor:
        menor = lista[y]

print(f"Lista de nombres:\n{lista}")
print(f"El menor alfabeticamente de esos nombres es: {menor}")