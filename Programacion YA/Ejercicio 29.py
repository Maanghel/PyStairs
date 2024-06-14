# Realizar un programa que lea los lados de n triángulos, e informar:
#       a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), 
#          isósceles (dos lados iguales), o escaleno (ningún lado igual)
#       b) Cantidad de triángulos de cada tipo.

tot_scal = 0
tot_equil = 0
tot_isos = 0

quantity = int(input("Enter the number of triangles to analyze:"))

for x in range(quantity):
    side1 = float(input("Enter the first side:"))
    side2 = float(input("Enter the second side:"))
    side3 = float(input("Enter the third side:"))
    
    if side1 == side2 and side1 == side3:
        print("Es un triangulo equilatero")
        tot_equil += 1
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print("Es un triangulo isósceles")
        tot_isos += 1
    else:
        print("Es un triangulo escaleno")
        tot_scal += 1

print(f"El total de triangulos equilateros fue de {tot_equil}")
print(f"El total de triangulos isosceles fue de {tot_isos}")
print(f"El total de triangulos escalenos fue de {tot_scal}")