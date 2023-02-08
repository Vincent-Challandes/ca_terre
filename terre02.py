# Function 
def afficheur_arguments():
    import sys
    arguments = sys.argv
    result =[]
    for i in arguments:
        if i == arguments[0]:
            continue
        else:
            result.append(i)
    return result

def print_list(a):
    for element in a:
        print(element)

# Resolution
resultat = afficheur_arguments()

# Display
print_list(resultat)
