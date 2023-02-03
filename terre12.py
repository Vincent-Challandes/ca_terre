import sys

# on récupère les arguments
arguments = sys.argv

# on check le nombre d'argument
nombre_arguments = len(arguments)

# si on nous a transmis 1 arguements (notre heure)
if nombre_arguments == 2:
    heure_saisi = arguments[1]
    heures = heure_saisi[0:2]
    minutes = heure_saisi[3:5]
    deux_point = heure_saisi[2:3]
    am_pm = heure_saisi[5:]
    nombre_caractere = len(heure_saisi)

    # on check qu'on nous ai bien donner une heure au format 12H de 12:00AM/11:59AM et 12:00PM/11:59PM
    if minutes.isdigit() and heures.isdigit() and deux_point == ":" and (am_pm == "AM" or am_pm == "PM"):
         heures = int(heures)
         minutes = int(minutes)

         # on contrôle que l'heure saisi soit entre 12:00AM/11:59AM et 12:00PM/11:59PM
         if 0 <= minutes <= 59 and 1 <= heures <= 12 :
             
            # on convertit le format 12h en 24h
             if  am_pm == "AM": 
                if heures == 12:
                    heures = 0
                else:
                    heures = heures

             else:
                 if heures == 12:
                     heures = heures
                 else:
                    heures = heures + 12

            # on force dans le cas ou les minutes ou les heures sont de zéro à 9 à écrire le premier zéro
             if 0 <= minutes <= 9:
                 minutes = f"0{minutes}"
            
             if 0 <= heures <= 9:
                 heures = f"0{heures}" 
        
             resultat = f"{heures}:{minutes}"
             print(resultat)    

         else:
            print("erreur pas les bon nombres veuillez entrer une heure format 12:00AM et 12:00PM inclu")
        
    else:
         print("erreur pas le bon format d'argument veuiller entrez une heure format 12:00AM et 12:00PM")     

else:
     print("erreur pas le bon nombre d'arguments veuillez saisir une heure au format 12h AM/PM")
