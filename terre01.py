chemin = __file__

#solution sans le module os 
chemin_liste = chemin.split("/") # joue pour mac pour windows il faudrait corriger le "/"
nom = chemin_liste[-1]
print(nom)

# solution avec module os
import os
nom_01 = os.path.basename(chemin)
print(nom_01)
