"""
Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. 
Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. Mostrar esta tercer lista.
"""

numeros1 = []
numeros2 = []

for x in range(4):
    valor = float(input("Ingrese un valor para la primer lista numerica: "))
    numeros1.append(valor)

    if x == 3:
        for y in range(4):
            valor = float(input("Ingrese un valor para la segunda lista numerica: "))
            numeros2.append(valor)

numeros3 = []
for z in range(4):
    valor = numeros1[z] + numeros2[z]
    numeros3.append(valor)

print("\tPrimer lista\tSegunda lista\t\t\tSuma")
for a in range(5):
    print(f"\t{numeros1[a]}\t\t{numeros2[a]}\t\t\t\t{numeros3[a]}")