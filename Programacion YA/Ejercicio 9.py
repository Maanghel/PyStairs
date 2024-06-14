# Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)

valor = int(input("Enter a number(negative, possitive or nule):"))

if valor > 0:
    print("The number is possitive")
elif valor < 0:
    print("the number is negative")
else:
    print("The number is nule")