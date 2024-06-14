""" 
Solicitar por teclado la cantidad de empleados que tiene la empresa. 
Crear y cargar una lista con todos los sueldos de dichos empleados. Imprimir la lista de sueldos ordenamos de menor a mayor.
"""

cantidad = int(input("Ingrese la cantidad de empleados que tiene la empresa: "))

sueldos = []

for x in range(cantidad):
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    sueldos.append(sueldo)

print(f"Lista de sueldos\n{sueldos}")

for y in range(cantidad - 1):
    for z in range(cantidad - y):
        if sueldos[z] > sueldos[z+1]:
            aux = sueldos[z]
            sueldos[z] = sueldos[z+1]
            sueldos[z+1] = aux

print(f"lista de sueldos ordenada de mayor a menor\n{sueldos}")