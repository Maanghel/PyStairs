# Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre 
# un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.

valor = int(input("Enter a number(one, two or three digits):"))

if valor > 99:
    print("The number have three digits")
elif valor < 100 and valor > 9:
    print("The number have two digits")
else:
    print("The number have a digit")