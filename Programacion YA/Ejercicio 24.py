# Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
# Emplear el operador “%” en la condición de la estructura condicional 
# (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
#       if valor%2==0:  

total_values = int(input("Enter the quantity of numbers:"))
par = 0
impar = 0
count = 1

while count <= total_values:
    value = int(input("Enter an integer:"))
    
    if value % 2 == 0:
        par += 1
    else:
        impar += 1
    
    count += 1

print(f"The total of even numbers was {par}")
print(f"The total of odd numbers was {impar}")