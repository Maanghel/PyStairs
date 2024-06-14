# Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio.

number1 = int(input("Introduzca el primer numero:"))
number2 = int(input("Introduzca el segundo numero:"))
number3 = int(input("Introduzca el tercero numero:"))
number4 = int(input("Introduzca el cuarto numero:"))

addition = number1 + number2 + number3 + number4
average = addition / 4

print("La suma de todos los valores es", addition)
print("El promedio de los valores es", average)