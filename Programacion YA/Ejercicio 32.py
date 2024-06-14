# Se cuenta con la siguiente información:
# Las edades de 5 estudiantes del turno mañana.
# Las edades de 6 estudiantes del turno tarde.
# Las edades de 11 estudiantes del turno noche.
# Las edades de cada estudiante deben ingresarse por teclado.
#       a) Obtener el promedio de las edades de cada turno (tres promedios)
#       b) Imprimir dichos promedios (promedio de cada turno)
#       c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.

prom_mañana = 0
prom_tarde = 0
prom_noche = 0

for x in range(5):
    valor = int(input("Ingrese la edad del alumno del turno de la mañana:"))
    
    prom_mañana += valor

for x in range(6):
    valor = int(input("Ingrese la edad del alumno del turno de la tarde:"))
    
    prom_tarde += valor 

for x in range(11):
    valor = int(input("Ingrese la edad del alumno del turno de la noche:"))
    
    prom_noche += valor

prom_mañana /= 5
prom_tarde /= 6
prom_noche /= 11

print(f"El promedio de edad de los alumnos de la mañana es de {prom_mañana}")
print(f"El promedio de edad de los alumnos de la tarde es de {prom_tarde}")
print(f"El promedio de edad de los alumnos de la noche es de {prom_noche}")

if prom_mañana > prom_noche and prom_mañana > prom_tarde:
    print("El turno de la mañana tiene el promedio de edades mayor.")
elif prom_tarde > prom_mañana and prom_tarde > prom_noche:
    print("El turno de la tarde tiene el promedio de edades mayor.")
elif prom_noche > prom_mañana and prom_noche > prom_tarde:
    print("El turno de la noche tiene el promedio de edades mayor.")
else:
    print("Los tres grupos tienen el mismo promedio de edades.")
