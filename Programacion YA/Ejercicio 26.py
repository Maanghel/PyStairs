# Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.

total = 0

for x in range(10):
    num = float(input("Enter a value:"))
    if x >= 5:
        total += num

print(f"The sum of the last 5 numbers is {total}")