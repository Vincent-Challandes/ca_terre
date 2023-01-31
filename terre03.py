import sys
arguments = sys.argv # on récupère les arguments donner par l'utilisateur

alphabet = "AbcdefghijKlmnopqrstuVwxyz".lower() # on créer la liste (chaine de caractère mais percu comme liste pour boucle)qu'on utilise pour boucler
#alphabet = alphabet.lower() # minuscule

lettre_depart = arguments[1].lower() # on isole la lettre de départ choisi par l'utilisateur
#lettre_depart = lettre_depart.lower() # minuscule comment ça même si l'utilisateur entre une majuscule ça fonctionne

if lettre_depart in alphabet: # on contrôle que l'arguement fasse parti de notre liste alphabet
    indice_départ = alphabet.index(lettre_depart) # on recherche la position de cettre lettre dans notre liste alphabet


    for i in alphabet[indice_départ:]: # on boucle dans notre liste alphabet depuis l'indice de départ jusqu'a la fin
        print(i, end = "") # on print sur la même ligne
    print() # retour a la ligne
