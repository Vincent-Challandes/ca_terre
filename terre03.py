## Function and variables globals
import sys

def affiche_alphabet_depuis():
    result = ""
    for i in alphabet[indice_départ:]: # on boucle dans notre liste alphabet depuis l'indice de départ jusqu'a la fin
        result += i
    return result
 
alphabet = "AbcdefghijKlmnopqrstuVwxyz".lower() 


## Error handling

# on cherche à savoir si un argument à été donné
# pour ça on va compté le nombre d'argument si nombre argument > 1 c'est qu'un argument à été donné
if len(sys.argv) != 2:
    print("erreur : Pas le bon nombre d'argument transmis au progamme.")
    sys.exit()

# on contrôle que l'arguement fasse parti de notre liste alphabet
if not sys.argv[1].lower() in alphabet: 
    print("erreur : Ce n'est pas une lettre de l'alphabet.")
    sys.exit()


## Parsing
lettre_depart = sys.argv[1].lower()
indice_départ = alphabet.index(lettre_depart) # on recherche la position de cettre lettre dans notre liste alphabet


## Resolution
resultat = affiche_alphabet_depuis()


## Display
print(resultat)
