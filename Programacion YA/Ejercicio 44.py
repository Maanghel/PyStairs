""" 
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) 
Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos.
"""

lista_mañana = []
lista_tarde = []

for x in range(4):
    valor = float(input("Introduzca el sueldo del empleado del turno matutino: "))
    lista_mañana.append(valor)
    
    if x == 3:
        for y in range(4):
            valor = float(input("Introduzca el sueldo del empleado del turno vespertino: "))
            lista_tarde.append(valor)

print(f"Lista de los sueldos del turno matutino\n{lista_mañana}")
print(f"Lista de los sueldos del turno vespertino\n{lista_tarde}")