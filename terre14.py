## Modules and Functions

import sys

def ctrl_isdigit(liste):
    all_digits = True
    for i in liste:
        if not str(i).isdigit():
            all_digits = False
            return all_digits
    return all_digits

def trie_pas_trie(liste, taille_liste):
    # ici on doit mettre -1 pour pas comparer la dernière valeur avec une valeur inexistante 
    for i in range(taille_liste -1):
        if int(liste[i]) > int(liste[i + 1]):
            return "Pas triée !"
    return "Triée !"


## Error handling

# s'assurer que l'utilisateur nous ai au moins transmis 2 nombres
if not len(sys.argv) >= 2:
    print("erreur : Veuillez entrer une liste d'au moins 2 nombres entiers")
    sys.exit()

# on check que chaque arguments soit un nombre avec une boucle for dans la fonction ctrl_isdigit()
if not ctrl_isdigit(sys.argv[1:]):
    print("erreur : Veuillez entrer une liste de nombre")
    sys.exit()


## Parsing

liste_de_nombre = sys.argv[1:]
taille_liste = len(sys.argv[1:])


## Resolution

resultat = trie_pas_trie(liste_de_nombre, taille_liste)


## Display 

print(resultat)
