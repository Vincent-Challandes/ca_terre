## Module Function and Variables globals

import sys

def pair_impair():
    if nombre % 2 == 0:
        return "pair"
    else:
        return "impair"


## Error handling

# on cherche à savoir si un argument à été donné
if len(sys.argv) != 2:
    print("erreur : Pas le bon nombre d'argument transmis au progamme.")
    sys.exit()

# on détermine si il s'agit d'un nombre ou pas (positif et négatif)
if not sys.argv[1].lstrip("-").isdigit():
    print("erreur : Ce n'est pas un nombre.")
    sys.exit()


## Parsing

nombre = int(sys.argv[1])


## Resolution

resultat = pair_impair()

## Display

print(resultat)
