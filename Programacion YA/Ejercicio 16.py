# Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y (distintos a cero).
# Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)

x = int(input("Enter the x coordinate:"))
y = int(input("Enter the y coordinate:"))

if x > 0 and y > 0:
    print("The point are in the first quadrant")
elif x < 0 and y > 0:
    print("The point are in the second quadrant")
elif x < 0 and y < 0:
    print("The point are in the third quadrant")
else:
    print("The point are in the fourth quadrant")