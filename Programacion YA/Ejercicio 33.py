""" 
Realizar un programa que solicite la carga de valores enteros por teclado y los sume. 
Finalizar la carga al ingresar el valor -1. Dejar como comentario dentro del código fuente el enunciado del problema.
"""

suma = 0

valor = int(input("Ingrese un numero entero (-1 para finalizar):"))

while valor != -1:
    suma += valor
    valor = int(input("Ingrese un numero entero (-1 para finalizar):"))

print(f"La suma de los valores ingresados fue de {suma}")