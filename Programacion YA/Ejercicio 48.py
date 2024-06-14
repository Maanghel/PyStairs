""" 
En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" 
si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.
"""

nombres = []
notas = []

for x in range(4):
    nom = input("Ingrese el nombre del alumno: ")
    nombres.append(nom)
    nota = float(input("Ingrese la nota del alumno (0-10): "))
    notas.append(nota)

print("Nombres de alumnos\tNotas de alumnos\tCondicion")
for y in range(4):
    print(f"\t{nombres[y]}\t\t\t{notas[y]}")
    
    if notas[y] >= 8:
        print(f"\t\t\t\t\t\tMuy bueno")
    elif notas[y] <= 7 and notas[y] >= 4:
        print(f"\t\t\t\t\t\tBueno")
    else:
        print(f"\t\t\t\t\t\tInsuficiente")