# Realizar la carga de dos nombres de personas distintos. Mostrar por pantalla luego ordenados en forma alfabética.

nom1 = input("Ingrese el primer nombre:")
nom2 = input("Ingrese el segundo nombre:")

if nom1 < nom2:
    print(f"{nom1}\n{nom2}")
else:
    print(f"{nom2}\n{nom1}")