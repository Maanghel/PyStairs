""" 
Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.
"""

lista = []
suma_sueldos = 0

for x in range(5):
    valor = float(input("Introduzca el sueldo del operario: "))
    
    suma_sueldos += valor
    
    lista.append(valor)

promedio = suma_sueldos / 5

print(f"Lista con los sueldos:\n{lista}")
print(f"El promedio de los sueldos es de {promedio}")