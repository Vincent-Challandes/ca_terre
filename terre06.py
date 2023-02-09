## Module, Function and Variables globals
import sys

def chaine_inversee(a):
    result = a[::-1]
    return result

## Error handling

if len(sys.argv) != 2:
    print("erreur : veuillez entrer une chaine de caractère entre guillemet \"Ma chaine de caractère\"")
    sys.exit()


## Parsing

chaine_recu = sys.argv[1]


## Resolution

resultat = chaine_inversee(chaine_recu)


## Display

print(resultat)
