# Function
def name_file_v1():
    #solution sans le module os 
    chemin_liste = chemin.split("/") # joue pour mac pour windows il faudrait corriger le "/"
    nom = chemin_liste[-1]
    return nom

def name_file_v2():
    # solution avec module os
    import os
    nom_1 = os.path.basename(__file__)
    return nom_1

def name_file_v3():
    # solution avec module sys
    import sys
    nom = sys.argv
    for i in nom:
        return i

# Variables
chemin = __file__

# Resolution
name_v1 = name_file_v1()
name_v2 = name_file_v2()
name_v3 = name_file_v3()

# Display
print(name_v1)
print(name_v2)
print(name_v3)
