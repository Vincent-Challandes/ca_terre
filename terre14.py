import sys

# on récupère les arguments
arguments = sys.argv
liste_original = arguments[1:]
liste_de_nombre = arguments[1:]

# on check le nombre d'argument
nombre_arguments = len(liste_de_nombre)

# s'assurer que l'utilisateur nous ai au moins transmis 2 nombres
if nombre_arguments >= 2:

# on check que chaque arguements soit un nombre avec une boucle for
    all_digits = True
    for i in liste_de_nombre:
        if not str(i).isdigit():
            all_digits = False
            break


    if all_digits:
     
    # on créer une première boucle avec un nombre de passage égale au nombre d'argument dans notre liste nombres
    # on fait ca car on doit passer la fonction de trie autant de fois qu'il y a d'argument afin d'être sur d'avoir passer tous les nombre avec chaque nombre
        for j in range(nombre_arguments):
             
        # puis on va créer un seconde boucle ou on va trié la liste
        # range(0, nombre_nombre - j -1) permet de partir du début de la liste et de finir à chaque tour 1 argument en moins (j) et le -1 c'est pour pas avoir l'erreur de comparer le dernier chiffre avec un arguements inexistant
        # on fait ça car à chaque tour on prend le plus grand nombre et on le met à la fin donc plus on avance plus la fin est dejà trié
            for i in range(0, nombre_arguments - j -1):
                 
        # ici la structure conditionnel va trié la liste 
                if int(liste_de_nombre[i]) > int(liste_de_nombre[i + 1]):
                   liste_de_nombre[i], liste_de_nombre[i + 1] = liste_de_nombre[i + 1], liste_de_nombre[i]

    # on check si la liste donnée par l'utilisateur était trié
        if liste_original == liste_de_nombre:
            print("Triée !")
        else:
            print("Pas triée !")   

    else:       
        print("erreur veuillez entrer une liste de nombre")
else:
    print("erreur veuillez entrer une liste d'au moins 2 nombre")
   