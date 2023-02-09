# Function 

import sys
def afficheur_arguments(a):
    result =[]
    for i in a:
        if i == arguments[0]:
            continue
        else:
            result.append(i)
    return result

def print_list(a):
    for element in a:
        print(element)


## Parsing

arguments = sys.argv


# Resolution
resultat = afficheur_arguments(arguments)


# Display
print_list(resultat)
