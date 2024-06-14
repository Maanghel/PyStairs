# Realizar un programa que solicite la carga por teclado de dos números, 
# si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar 
# el producto y la división del primero respecto al segundo.

valor1 = int(input("Introduzca el primer numero:"))
valor2 = int(input("Introduzca el segundo numero:"))

if valor1 > valor2:
    addition = valor1 + valor2
    substraction = valor1 - valor2
    
    print("La suma de los dos numeros es:", addition)
    print("La resta de los dos numeros es:", substraction)
else:
    multiplication = valor1 * valor2
    division = valor2 / valor1
    
    print("La multilpicacion de los dos numeros es:", multiplication)
    print("La division de los dos numeros es:", division)