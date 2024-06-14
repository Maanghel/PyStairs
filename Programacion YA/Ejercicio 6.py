# Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado".

note1 = int(input("Ingrese la nota de un alumno:"))
note2 = int(input("Ingrese la nota de un alumno:"))
note3 = int(input("Ingrese la nota de un alumno:"))

average = (note1 + note2 + note3)/ 3

if average >= 7:
    print("Promocionado")