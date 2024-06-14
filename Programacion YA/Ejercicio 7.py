# Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) 
# mostrar un mensaje indicando si el número tiene uno o dos dígitos.
# (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

number = int(input("Enter a number:"))

if number > 9:
    print("The number have two digits")
else:
    print("The number have a digit")