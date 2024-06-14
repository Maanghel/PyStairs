# Realizar un programa que permita cargar dos listas de 15 valores cada una. 
# Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor 
# (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
# Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

total_list1 = 0
total_list2 = 0
count = 1

while count <= 15:
    value = int(input("Enter a value for the first list:"))
    total_list1 += value
    count += 1

count = 1

while count <= 15 :
    value = int(input("Enter a value for the second list:"))
    total_list2 += value
    count += 1

if total_list1 > total_list2:
    print("The first list is larger than the second")
elif total_list2 > total_list1:
    print("The second list is larger than the first")
else:
    print("Both lists are equal")