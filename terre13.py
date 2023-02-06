import sys

# on récupère les arguments
arguments = sys.argv

# on check le nombre d'argument
nombre_arguments = len(arguments)

# si on nous a transmis 3 arguements (nos 3 entiers)
if nombre_arguments == 4:
    a = arguments[1]
    b = arguments[2]
    c = arguments[3]

    # on check qu'on nous ai bien donner 3 nombres entiers
    if a.isdigit() and b.isdigit() and c.isdigit():
         
         a = int(a) #doit être converti en integer
         b = int(b)
         c = int(c)
         nombres = [a, b, c]
         nombre_nombre = len(nombres)
        
        # on créer une première boucle avec un nombre de passage égale au nombre d'argument dans notre liste nombres
        # on fait ca car on doit passer la fonction de trie autant de fois qu'il y a d'argument afin d'être sur d'avoir passer tous les nombre avec chaque nombre
         for j in range(nombre_nombre):
             
             # puis on va créer un seconde boucle ou on va trié la liste
             # range(0, nombre_nombre - j -1) permet de partir du début de la liste et de finir à chaque tour 1 argument en moins (j) et le -1 c'est pour pas avoir l'erreur de compérer le dernier chiffre avec un arguements inexistant
             # on fait ça car à chaque tour on prend le plus grand nombre et on le met à la fin donc plus on avance plus la fin est dejà trié
             for i in range(0, nombre_nombre - j -1):
                 
                 # ici la structure conditionnel va trié la liste
                 # par-contre le cas ou deux nombre sont égaux on break pour sortir de la première boucle 
                 if nombres[i] == nombres[i + 1]:
                     print("erreur deux fois le même nombre")
                     break
                 elif nombres[i] > nombres[i + 1]:
                   nombres[i], nombres[i + 1] = nombres[i + 1], nombres[i]

             # on break pour sortir de la seconde boucle
             if nombres[i] == nombres[i + 1]:
                break    
              
         if not nombres[i] == nombres[i + 1]:
            print(nombres[1])


         
        
    else:
         print("erreur pas le bon format d'argument veuiller entrez 3 nombre entier")     

else:
     print("erreur pas le bon nombre d'arguments veuillez saisir 3 nombres entier")
