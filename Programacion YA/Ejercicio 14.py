# Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, 
# imprimir en pantalla la leyenda "Alguno de los números es menor a diez".

valor1 = int(input("Enter the first valor:"))
valor2 = int(input("Enter the second valor:"))
valor3 = int(input("Enter the third valor:"))

if valor1 < 10 or valor2 < 10 or valor3 < 10:
    print("Some number are less than 10")