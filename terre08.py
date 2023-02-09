## Modules, Functions and Variables globals

import sys

def puissance_dun_nombre(a, b):
     isolé_a = a
     for i in range(b - 1):
          a = a * isolé_a
     return a


## Error handling

# si on nous a transmis 2 arguements (nos deux nombres pour notre calcul de puissance)
if len(sys.argv) != 3:
     print("erreur : Pas le bon nombre d'arguments veuillez entrer 2 nombres entiers")
     sys.exit()

# on contrôle que ce soit des nombre et que l'exposant soit positif
if not sys.argv[1].lstrip("-").isdigit() or not sys.argv[2].isdigit():
     print("erreur : Les arguement doivent être des nombre et l'exposant doit être positif")
     sys.exit()


## Parsing

nombre, exposant = int(sys.argv[1]), int(sys.argv[2])


## Resolution

resultat = puissance_dun_nombre(nombre, exposant)


## Display

print(resultat)
