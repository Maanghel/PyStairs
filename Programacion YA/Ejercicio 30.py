# Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
# Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. 
# Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

cantidad = int(input("Ingrese el total de puntos a procesar:"))

primer_cuadrante = 0
segundo_cuadrante = 0
tercer_cuadrante = 0
cuarto_cuadrante = 0

for x in range(cantidad):
    x_coor = int(input("Ingrese el valor de la coordenada x:"))
    y_coor = int(input("Ingrese el valor de la coordenada y:"))
    
    if x_coor > 0 and y_coor > 0:
        primer_cuadrante += 1
    elif x_coor < 0 and y_coor > 0:
        segundo_cuadrante += 1
    elif x_coor < 0 and y_coor < 0:
        tercer_cuadrante += 1
    else:
        cuarto_cuadrante += 1

print(f"El total de puntos en el primer cuadrante son de {primer_cuadrante}")
print(f"El total de puntos en el segundo cuadrante son de {segundo_cuadrante}")
print(f"El total de puntos en el tercer cuadrante son de {tercer_cuadrante}")
print(f"El total de puntos en el cuarto cuadrante son de {cuarto_cuadrante}")