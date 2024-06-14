# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, 
# realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos 
# empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa 
# deberá informar el importe que gasta la empresa en sueldos al personal.

num_person = int(input("Enter the number of persons:"))
count = 1
low_salary = 0
high_salary = 0
total_salary = 0

while count <= num_person:
    salary = float(input("enter the person's salary ($100-$500):"))
    if salary >= 100 and salary <= 300:
        low_salary += 1
        total_salary += salary
    elif salary > 300 and salary <= 500:
        high_salary += 1
        total_salary += salary
    else:
        print("Error. Enter a salary between $100 and $500.")
    count += 1

print(f"the number of people who have a salary between $100 and $300 is of {low_salary}")
print(f"the number of people who have a salary between $301 and $500 is of {high_salary}")
print(f"The company spends a total of ${total_salary} on salaries.")