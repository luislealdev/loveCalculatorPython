print("Welcome to Love Calculator")
name1 = input("Enter name one: ")
name2 = input("Enter name two: ")

#TRUE LOVE
name1 = name1.lower()
name2 = name2.lower()

#TRUE
contadorTrueName1 = int(name1.count('t')) + int(name1.count('r')) + int(name1.count('u')) + int(name1.count('e'))
contadorTrueName2 = int(name2.count('t')) + int(name2.count('r')) + int(name2.count('u')) + int(name2.count('e'))

contadorTotalTrue = str(contadorTrueName1+contadorTrueName2)

#LOVE
contadorLoveName1 = int(name1.count('l')) + int(name1.count('o')) + int(name1.count('v')) + int(name1.count('e'))
contadorLoveName2 = int(name2.count('l')) + int(name2.count('o')) + int(name2.count('v')) + int(name2.count('e'))

contadorTotalLove = str(contadorLoveName1+contadorLoveName2)

if int(contadorTotalTrue+contadorTotalLove) <10 or int(contadorTotalTrue+contadorTotalLove) > 90:
    print("You are like Coke and Mentos")
elif int(contadorTotalTrue+contadorTotalLove) > 40 and int(contadorTotalTrue+contadorTotalLove) < 50:
    print("You look cool together")

print("El porcentaje de compatibilidad es "+contadorTotalTrue+contadorTotalLove+"%")