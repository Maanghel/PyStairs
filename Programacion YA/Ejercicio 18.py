# Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

count = 1
approved = 0
failed = 0

while count <= 10:
    valor = int(input("Enter the student's score:"))
    if valor >= 7:
        approved += 1
    else:
        failed += 1
    count += 1

print(f"The number of approved students was {approved}")
print(f"The number of students who failed was of {failed}")