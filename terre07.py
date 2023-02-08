## Modules, Functions and Variables globals
import sys

def taille_chaine(a):
     nb_caratere = 0
     for i in a:
          nb_caratere += 1
     return nb_caratere


## Error handling

if len(sys.argv) != 2:
     print("erreur : veuillez entrer une chaine de caractère entre guillemet \"Ma chaine de caractère\"")
     sys.exit()

if sys.argv[1].lstrip("-").isdigit():
     print("erreur : il s'agit d'un nombre on souhaite une chaine de caractère entre des \" \" ")
     sys.exit()


## Resolution

resultat = taille_chaine(sys.argv[1])


## Display

print(resultat)
