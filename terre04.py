import sys

# on récupère la liste des arguments
arguments = sys.argv

# on cherche à savoir si un argument à été donné
# pour ça on va compté le nombre d'argument si nombre argument > 1 c'est qu'un argument à été donné
nombre_arguments = len(arguments)

# on détermine si il ya bien eu un argument donné
if nombre_arguments == 2:
    argument = arguments[1]

    # on détermine si il s'agit d'un nombre ou pas (positif et négatif) 
    if argument.lstrip("-").isdigit():
        argument = int(argument)
        if argument % 2 == 0:
            print("pair")
        else:
            print("impair")
    else:
        print("ce n'est pas un nombre.")        
else:
    print("Pas le bon nombre d'argument transmis au progamme.")
    