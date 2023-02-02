import sys

# on récupère les arguments
arguments = sys.argv

# on check le nombre d'argument
nombre_arguments = len(arguments)

# si on nous a transmis 1 arguements (notre nombre à checker)
if nombre_arguments == 2:
    nombre_1 = arguments[1]
    # on contrôle que ce soit un nombre entier positif
    if nombre_1.isdigit():
         nombre_1 = int(nombre_1)
         # on va contrôler si c'est un nombre premier
         if nombre_1 > 2:
            # on créer une boucle ou l'on cherche a savoir si on peut diviser notre nombre par autre choses que lui-même et et 1 
            for i in range(2, nombre_1):
                division = nombre_1 % i
                if division == 0:
                    break
            # si le reste est 0 c'est que c'est divisible donc non premier
            if division == 0:
                print(f"Non, {nombre_1} n'est pas un nombre premier.")
            else:
                print(f"Oui, {nombre_1} est un nombre premier.")

         elif nombre_1 == 2: # le 2 est géré a part car dans la boucle 2 % 2 ca donne un reste de 0 mais c'est tous de même un nombre premier
            print(f"Oui, {nombre_1} est un nombre premier.")

         else:
            print(f"Non, {nombre_1} n'est pas un nombre premier.")
         
              
              
          
    else:
          print("erreur l'arguement doit être un nombre entier positif")
    
else:
     print("erreur pas le bon nombre d'arguments")
