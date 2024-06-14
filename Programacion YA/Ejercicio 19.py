# Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

num_person = int(input("Enter the number of persons:"))
count = 1
total = 0

while count <= num_person:
    height = float(input("Enter the person height:"))
    total += height
    count += 1

average = total / num_person
print(f"The average height is {average}")