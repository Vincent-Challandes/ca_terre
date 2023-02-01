import sys

# on récupère les arguments
arguments = sys.argv

# on check le nombre d'argument
nombre_arguments = len(arguments)

# si on nous a transmis 1 arguement (Notre chaine de caractère) on va print l'inverse de la chaine de caractère
if nombre_arguments == 2:
    chaine_de_caractere = arguments[1]
    print(chaine_de_caractere[::-1]) # on passe à travers notre chaine de caractère comme un liste [::-1] qui veut dire du début à la fin avec un pas de -1 soit de la fin au début
    
else:
     print("erreur veuillez entrer une chaine de caractère entre des \" \" ")

