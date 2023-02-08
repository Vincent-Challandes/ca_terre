## Module, Function and Variables globals
import sys

def chaine_inversee(a):
    result = a[::-1]
    return result

## Error handling

if len(sys.argv) != 2:
    print("erreur : veuillez entrer une chaine de caractère entre guillemet \"Ma chaine de caractère\"")
    sys.exit()


## Resolution

resultat = chaine_inversee(sys.argv[1])


## Display

print(resultat)
