# Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a 
# la medida de la base y la altura de un triángulo. El programa deberá informar:
#   a) De cada triángulo la medida de su base, su altura y su superficie.
#   b) La cantidad de triángulos cuya superficie es mayor a 12.

total = 0

quantity = int(input("Enter the number of triangles to enter:"))

for x in range(quantity):
    base = float(input("Enter the base of the triangle:"))
    height = float(input("Enter the height of the triangle:"))
    
    surface = (base * height) / 2
    
    print(f"The triangle base is {base}")
    print(f"The triangle height is {height}")
    print(f"The area of the triangle is {surface}")
    if surface > 12:
        total += 1

print(f"The total number of triangles with a surface area greater than 12 were {total}")