# Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad.

day = int(input("Enter the number day:"))
month = int(input("Enter the number month:"))
year = int(input("Enter the number year:"))

if day == 25 and month == 12:
    print("Merry Christmas")