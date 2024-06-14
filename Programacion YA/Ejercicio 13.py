# Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, 
# imprimir en pantalla la leyenda "Todos los números son menores a diez".

valor1 = int(input("Enter the first valor:"))
valor2 = int(input("Enter the second valor:"))
valor3 = int(input("Enter the third valor:"))

if valor1 < 10 and valor2 < 10 and valor3 < 10:
    print("All number are less than 10")