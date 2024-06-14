# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#       a) La cantidad de valores ingresados negativos.
#       b) La cantidad de valores ingresados positivos.
#       ) La cantidad de múltiplos de 15.
#       d) El valor acumulado de los números ingresados que son pares.

tot_pares = 0
tot_neg = 0
tot_pos = 0
tot_mult = 0

for x in range (10):
    valor = int(input("Ingrese un valor:"))
    
    if valor > 0:
        tot_pos += 1
    else:
        tot_neg += 1
    if valor % 15 == 0:
        tot_pos += 1
    if valor % 2 == 0:
        tot_pares += valor

print(f"El total de valores negativos fueron {tot_neg}")
print(f"El total de valores positivos fueron {tot_pos}")
print(f"El total de valores multiplos de 15 fueron {tot_mult}")
print(f"El total de la suma de los valores que eran pares fueron {tot_pares}")