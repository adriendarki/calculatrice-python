import re

print("Calculatrice magique !")
print("Ecris 'quitter' pour sortir du programme. Bon calcule ! \n")

previous = 0
run = True


def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Entrer l'équation:")
    else:
        equation = input(str(previous))

    if equation == 'quitter':
        print("Au revoir ! :) ")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()
