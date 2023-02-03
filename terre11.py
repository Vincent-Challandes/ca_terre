import sys

# on récupère les arguments
arguments = sys.argv

# on check le nombre d'argument
nombre_arguments = len(arguments)

# si on nous a transmis 1 arguements (notre heure)
if nombre_arguments == 2:
    heure_saisi = arguments[1]
    heures = heure_saisi[0:2]
    minutes = heure_saisi[3:]
    deux_point = heure_saisi[2:3]
    nombre_caractere = len(heure_saisi)

    # on check qu'on nous ai bien donner une heure au format 24 de 00:00 à 23:59
    if minutes.isdigit() and heures.isdigit() and deux_point == ":" and nombre_caractere == 5:
         heures = int(heures)
         minutes = int(minutes)

         # on contrôle que l'heure saisi soit entre 00:00 et 23:59
         if 0 <= minutes <= 59 and 0 <= heures <= 23:
             
            # on convertit le format 24h en 12h
             if  heures < 12:
                am_pm = "AM" 
                if heures == 0:
                    heures = 12
             else:
                 am_pm = "PM"
                 if heures == 12:
                     heures = heures
                 else:
                    heures = heures -12

            # on force dans le cas ou les minutes ou les heures sont de zéro à 9 écrire le premier zéro
             if 0 <= minutes <= 9:
                 minutes = f"0{minutes}"
            
             if 1 <= heures <= 9:
                 heures = f"0{heures}" 
        
             resultat = f"{heures}:{minutes}{am_pm}"
             print(resultat)    

         else:
            print("erreur veuillez entrer une heure entre 00:00 et 23:59 inclu")
        
    else:
         print("erreur pas le bon format d'argument veuiller entrez une heure entre 00:00 et 23:59")     

else:
     print("erreur pas le bon nombre d'arguments veuillez saisir une heure au format 24h")
