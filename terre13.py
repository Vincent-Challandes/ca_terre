## Modules and Functions

import sys

def trouver_suisse(nombres, nombre_nombre):
    # on créer une première boucle avec un nombre de passage égale au nombre d'argument dans notre liste nombres
    # on fait ca car on doit passer la fonction de trie autant de fois qu'il y a d'argument afin d'être sur d'avoir passer tous les nombre avec chaque nombre
    for j in range(nombre_nombre):
             
        # puis on va créer un seconde boucle ou on va trié la liste
        # range(0, nombre_nombre - j -1) permet de partir du début de la liste et de finir à chaque tour 1 argument en moins (j) et le -1 c'est pour pas avoir l'erreur de compérer le dernier chiffre avec un arguements inexistant
        # on fait ça car à chaque tour on prend le plus grand nombre et on le met à la fin donc plus on avance plus la fin est dejà trié
        for i in range(0, nombre_nombre - j -1):
                 
            # ici la structure conditionnel va trié la liste
            # par-contre le cas ou deux nombre sont égaux on retourne un erreur
            if nombres[i] == nombres[i + 1]:
                return "erreur : deux fois le même nombre"
                 
            elif nombres[i] > nombres[i + 1]:
                nombres[i], nombres[i + 1] = nombres[i + 1], nombres[i]
    
    # on retourne le chiffre central de la liste nombres
    return nombres[1]
        

## Error handling

# check si on nous a transmis 3 arguements (nos 3 entiers)
if len(sys.argv) != 4:
    print("erreur : Pas le bon nombre d'arguments veuillez saisir 3 nombres entier")
    sys.exit()

# on check qu'on nous ai bien donner 3 nombres entiers
if not sys.argv[1].isdigit() or not sys.argv[2].isdigit() or not sys.argv[3].isdigit():
    print("erreur : Pas le bon format d'argument veuiller entrez 3 nombre entier positif")
    sys.exit()


## Parsing

nombres = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]

nombre_nombre = len(nombres)


## Resolution

resultat = trouver_suisse(nombres, nombre_nombre)


## Display

print(resultat)
