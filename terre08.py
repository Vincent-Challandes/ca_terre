import sys

# on récupère les arguments
arguments = sys.argv

# on check le nombre d'argument
nombre_arguments = len(arguments)

# si on nous a transmis 2 arguements (nos deux nombres pour notre calcul de puissance)
if nombre_arguments == 3:
    nombre_1 = arguments[1]
    nombre_2 = arguments[2]
    # on contrôle que ce soit des nombre et que l'exposant soit positif
    if nombre_1.lstrip("-").isdigit() and nombre_2.isdigit():
         resultat = int(nombre_1) ** int(nombre_2)
         print(resultat)
    else:
         print("erreur les arguement doivent être des nombre et l'exposant doit être positif")
    
else:
     print("erreur pas le bon nombre d'arguments")
