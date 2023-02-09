## Modules and Functions

import sys

def racine_carre(a):
     result = a ** 0.5
     return result


def racine_carre_manuelle(a):
    # initialiser les valeurs minimales et maximales pour la bissection
    min_val = 0
    max_val = a

    # définir une précision pour la méthode de bissection
    precision = 0.0001

    # utiliser la méthode de bissection pour trouver la racine carrée
    while (max_val - min_val) > precision:
        # trouver la valeur moyenne entre les valeurs minimale et maximale
        moyenne = (min_val + max_val) / 2
        carre = moyenne * moyenne

        # déterminer si la valeur moyenne est plus grande ou plus petite que a
        if carre < a:
            min_val = moyenne
        else:
            max_val = moyenne
    
    # retourner la valeur moyenne finale comme la racine carrée
    return moyenne


## Error handling

# chek nb arguements
if len(sys.argv) != 2:
    print("erreur : Pas le bon nombre d'arguments veuillez entrer un nombre entier positif")
    sys.exit()

# on contrôle que ce soit un nombre entier positif
if not sys.argv[1].isdigit():
     print("erreur : L'arguement doit être un nombre entier positif")
     sys.exit()
    
    
## Parsing

nombre = int(sys.argv[1])


## Resolution

resultat = racine_carre(nombre)

resultat_manuel = racine_carre_manuelle(nombre)

resultat_arrondit = round(resultat)

resultat_manuel_arrondit = round(resultat_manuel)


## Display

print(resultat) 
print(resultat_arrondit)

print(resultat_manuel) 
print(resultat_manuel_arrondit)
