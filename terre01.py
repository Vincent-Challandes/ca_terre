# Function
def name_file_v1():
    #solution sans le module os 
    chemin_liste = chemin.split("/") # joue pour mac pour windows il faudrait corriger le "/"
    nom = chemin_liste[-1]
    print(nom)

def name_file_v2():
    # solution avec module os
    import os
    nom = os.path.basename(__file__)
    print(nom)

def name_file_v3():
    # solution avec module sys
    import sys
    nom = sys.argv
    for i in nom:
        print(i)

# Variables
chemin = __file__

# Resolution
name_file_v1()
name_file_v2()
name_file_v3()
