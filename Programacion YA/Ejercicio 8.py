# Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.

valor1 = int(input("Enter the first valor:"))
valor2 = int(input("Enter the second valor:"))
valor3 = int(input("Enter the third valor:"))

if valor1 > valor2:
    if valor1 > valor3:
        print("The first valor is the largest")
    else:
        print("The second valor is the largest")
elif valor2 > valor3:
    print("The second valor is the largest")
else:
    print("The third valor is the largest")