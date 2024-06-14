# Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero 
# con el segundo y a este resultado se lo multiplica por el tercero.

valor1 = int(input("Enter the first valor:"))
valor2 = int(input("Enter the second valor:"))
valor3 = int(input("Enter the third valor:"))

if valor1 == valor2 and valor2 == valor3:
    addition = valor1 + valor2
    multiplication = addition * valor3
    
    print(f"The addition of the first two:{addition}")
    print(f"The multiplication of the addition by the third valor:{multiplication}")