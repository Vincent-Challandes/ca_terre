import sys

# on récupère les arguments
arguments = sys.argv

# on check les nombre d'argument
nombre_arguments = len(arguments)

# si on nous a transmis 2 nombre on passe au opération
if nombre_arguments == 3:
    arg1 = arguments[1]
    arg2 = arguments[2]

    # on check que nos 2 arguments soit des nombres
    if arg1.isdigit() and arg2.isdigit():
        
        # convertir nos argument en integer
        arg1 = int(arg1)
        arg2 = int(arg2)
        
        # on mais la condition pour qu'on ai arg1 plus grand que arg2 et pas de 0
        if arg1 > arg2 and arg2 > 0:
            reslutat = arg1 // arg2
            reste = arg1 % arg2
            print(f"résultat : {reslutat}")
            print(f"reste : {reste}")
        else:
            print("erreur de calcul")
    else:
        print("erreur pas des nombres")
else:
    print("erreur pas le bon nombre d'arguments")
