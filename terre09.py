## Modules and Functions

import sys

def racine_carre(a):
     result = a ** 0.5
     return result


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


## Display

print(resultat) # résultat du float donc nombre décimal
resultat = int(resultat) # on ramene le float à un integer
print(resultat) # résultat du integer donc nombre entier
