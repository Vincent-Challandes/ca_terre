## Modules and Functions

import sys


### fonctions de contrôle
def ctrl_format(a):
    # on check qu'on nous ai bien donner une heure au format 12H de 12:00AM/11:59AM et 12:00PM/11:59PM
    if not a[3:5].isdigit() or not a[0:2].isdigit() or not a[2:3] == ":" or not (a[5:] == "AM" or a[5:] == "PM"):
        print("erreur : Pas le bon format d'argument veuiller entrez une heure format 12:00AM et 12:00PM")
        sys.exit()

def ctrl_heure_exist(a):
    if not 0 <= int(a[3:5]) <= 59 or not 1 <= int(a[0:2]) <= 12 :
        print("erreur : Heure inexistante veuillez entrer une heure format 12:00AM et 12:00PM inclu")
        sys.exit()


### fonction de résolution
def convertisseur(heures, am_pm):
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
     
     return heures

def heure_format_24(heures, minutes):
    heures = str(heures).zfill(2)
    minutes = str(minutes).zfill(2)
    return f"{heures}:{minutes}"


## Error handling
# si on nous a transmis 1 arguements (notre heure)
if len(sys.argv) != 2:
    print("erreur : Pas le bon nombre d'arguments veuillez saisir une heure au format 12h AM/PM")
    sys.exit()

# check format de l'argument
ctrl_format(sys.argv[1])

# check que l'argument soit une heure au format 12h
ctrl_heure_exist(sys.argv[1])


## Parsing

heures = int(sys.argv[1][0:2])
minutes = int(sys.argv[1][3:5])
am_pm = sys.argv[1][5:]


## Resolution

heure_converti = convertisseur(heures, am_pm)
        
resultat = heure_format_24(heure_converti, minutes)


## Display

print(resultat)
 