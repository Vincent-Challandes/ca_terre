# Function 
def afficheur_arguments():
    import sys
    arguments = sys.argv
    for i in arguments:
        if i == arguments[0]:
            continue
        else:
            print(i)

# Resolution
afficheur_arguments()
