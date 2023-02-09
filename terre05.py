## Module, Function and Variables globals

import sys

def division(a, b):
     reslutat = a // b
     return reslutat

def reste(a, b):
     reste = a % b
     return reste


## Error handling

# check si on nous a transmis 2 arguments
if len(sys.argv) != 3:
    print("erreur : Pas le bon nombre d'arguments")
    sys.exit()

# on check que nos 2 arguments soit des nombres
if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("erreur : Ce n'est pas deux nombres")
    sys.exit()

# on mais la condition pour qu'on ai arg1 plus grand que arg2 et pas de 0
if int(sys.argv[1]) < int(sys.argv[2]) or int(sys.argv[2]) == 0:
    print("erreur : premier nombre plus grand que le second ou second égal à zéro")
    sys.exit()


# Parsing

arg1, arg2 = int(sys.argv[1]), int(sys.argv[2])


# Resolution 

resultat = division(arg1, arg2)
reste = reste(arg1, arg2)


## Display
          
print(f"résultat : {resultat}")
print(f"reste : {reste}")
       