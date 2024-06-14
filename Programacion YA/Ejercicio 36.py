"""
Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es ""
"""

cantidad = 0

oracion = input("Ingrese una oracion:")

for x in range(len(oracion)):
    if oracion[x] == " ":
        cantidad += 1

print(f"La cantidad de espacios en blanco que contiene la oracion son {cantidad}")