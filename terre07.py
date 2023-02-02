import sys

# on récupère les arguments
arguments = sys.argv

# on check le nombre d'argument
nombre_arguments = len(arguments)

# si on nous a transmis 1 arguement (Notre chaine de caractère)
if nombre_arguments == 2:
    chaine_de_caractere = arguments[1]
    if chaine_de_caractere.lstrip("-").isdigit():
         print("erreur il s'agit d'un nombre on souhaite une chaine de caractère entre des \" \" ")
    else:
         # on check le nombre de caractère
         nombre_caractere = len(chaine_de_caractere)
         print(nombre_caractere)
    
else:
     print("erreur veuillez entrer une chaine de caractère entre des \" \" ")
