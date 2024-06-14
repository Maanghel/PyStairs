""" 
Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.
"""

lista = []
suma_alturas = 0

for x in range(5):
    valor = float(input("Ingrese la altura de la persona:"))
    lista.append(valor)
    
    suma_alturas += valor

total_altas = 0
total_bajas = 0

promedio = suma_alturas / 5

for x in range(len(lista)):
    if lista[x] > promedio:
        total_altas += 1
    elif lista[x] < promedio:
        total_bajas += 1

print(f"La cantidad de personas con la altura mayor al promedio es de {total_altas}")
print(f"La cantidad de personas con la altura menor al promedio es de {total_bajas}")