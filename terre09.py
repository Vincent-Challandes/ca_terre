import sys

# on récupère les arguments
arguments = sys.argv

# on check le nombre d'argument
nombre_arguments = len(arguments)

# si on nous a transmis 1 arguements (notre nombre pour notre calcul de racine carré)
if nombre_arguments == 2:
    nombre_1 = arguments[1]
    # on contrôle que ce soit un nombre entier positif
    if nombre_1.isdigit():
         nombre_1 = int(nombre_1)
         resultat = nombre_1 ** 0.5
         print(resultat) # résultat du float donc nombre décimal
         resultat = int(resultat) # on ramene le float à un integer
         print(resultat) # résultat du integer donc nombre entier 
    else:
         print("erreur l'arguement doit être un nombre entier positif")
    
else:
     print("erreur pas le bon nombre d'arguments")
