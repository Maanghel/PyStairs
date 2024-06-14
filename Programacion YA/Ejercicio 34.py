"""
Confeccionar un programa que solicite la carga de 10 valores reales por teclado. 
Mostrar al final su suma. Definir varias líneas de comentarios 
indicando el nombre del programa, el programador y la fecha de la última modificación. Utilizar el caracter # para los comentarios.
"""

# Nombre del programa: Ingrese 10 numeros
# Programador: Manuel Angel Pesqueira Gamez
# Ultima actualizacion: 30/05/2024

suma = 0

for x in range(10):
    valor = float(input("Ingrese un numero real:"))
    
    suma += valor

print(f"El valor de la suma de los valores ingresados es de {suma}")