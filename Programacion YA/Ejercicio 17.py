# De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe:
#   a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
#   b) Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
#   c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.

salary = float(input("Enter the employee's salary:"))
year = int(input("Enter the employee's years of seniority:"))

if salary < 500 and year >= 10:
    increase = salary * 0.20
    salary += increase
    
    print(f"The employee's new salary:{salary}")
elif salary < 500 and year < 10:
    increase = salary * 0.05
    salary += increase
    
    print(f"The employee's new salary:{salary}")
else:
    print(f"The employee's new salary:{salary}")