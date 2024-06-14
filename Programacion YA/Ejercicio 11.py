# Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: 
# cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. 
# Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo 
# según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:
#       Nivel máximo:	Porcentaje>=90%.
#   	Nivel medio:	Porcentaje>=75% y <90%.
#   	Nivel regular:	Porcentaje>=50% y <75%.
#   	Fuera de nivel:	Porcentaje<50%.

total_question = int(input("Enter the total number of questions:"))
correct_questions = int(input("Enter the total number of correct questions:"))

percentaje = (correct_questions * 100) / total_question

if percentaje >= 90:
    print("Maximum level")
elif percentaje >= 75 and percentaje < 90:
    print("Medium level")
elif percentaje >= 50 and percentaje < 75:
    print("Regular level")
else:
    print("Out of level")