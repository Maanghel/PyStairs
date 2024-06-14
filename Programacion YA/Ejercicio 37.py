"""
Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. 
Contar la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas 
para que sea más fácil disponer la condición que verifica que es una vocal.
"""

oracion1 = input("Ingrese una oracion:")

oracion2 = oracion1.lower()

cantidad = 0

for x in range(len(oracion2)):
    if oracion2[x] == "a" or oracion2[x] == "e" or oracion2[x] == "i" or oracion2[x] == "o" or oracion2[x] == "u":
        cantidad += 1

print(f"La cantidad de vocales que tiene la oracion es de {cantidad}")