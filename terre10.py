## Modules and Functions
import sys

def nb_premier(a):
    if a > 2:
        # on créer une boucle ou l'on cherche a savoir si on peut diviser notre nombre par autre choses que lui-même et et 1 
        for i in range(2, a):
            reste = a % i
            if reste == 0:
                break
             # si le reste est 0 c'est que c'est divisible donc non premier
        if reste == 0:
            return f"Non, {a} n'est pas un nombre premier."
        else:
            return f"Oui, {a} est un nombre premier."

    elif a == 2: # le 2 est géré a part car dans la boucle 2 % 2 ca donne un reste de 0 mais c'est tous de même un nombre premier
        return f"Oui, {a} est un nombre premier."

    else:
        return f"Non, {a} n'est pas un nombre premier."


## Error handling

# check nb arguements
if len(sys.argv) != 2:
    print("erreur : Pas le bon nombre d'arguments veuillez entrer un nombre entier positif")
    sys.exit()

if not sys.argv[1].isdigit():
    print("erreur : L'arguement doit être un nombre entier positif")
    sys.exit()


## Parsing

nombre = int(sys.argv[1])


## Resolution 

resultat = nb_premier(nombre)


## Display

print(resultat)
