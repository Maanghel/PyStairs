# Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora.

amount_hours = int(input("Introduzca la cantidad de horas trabajadas del empleado:"))
pay_hours = float(input("Introduzca el pago por hora del empleado:"))

mensual_salary = amount_hours * pay_hours

print("El sueldo mensual del empleado es", mensual_salary)