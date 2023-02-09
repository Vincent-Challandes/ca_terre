## Modules and Functions

import sys


### fonction de contrôle
def ctrl_format(a):
    # on check qu'on nous ai bien donner une heure au format 24 de 00:00 à 23:59
    if not a[3:].isdigit() or not a[0:2].isdigit() or not a[2:3] == ":" or not len(a) == 5:
        print("erreur : Pas le bon format d'argument veuiller entrez une heure entre \"00:00\" et \"23:59\"")
        sys.exit()


def ctrl_heure_exist(a):
    if not 0 <= int(a[3:]) <= 59 or not 0 <= int(a[0:2]) <= 23:
        print("erreur : Heure inexistante veuillez entrer une heure entre \"00:00\" et \"23:59\" inclu")
        sys.exit()


### fonction de résolution
def convertisseur_24_12(heures):
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
    return heures, am_pm

# cette fonction remet l'heure dans l'ordre et au bon format
def heure_format_12(heures, minutes, am_pm):
    heures = str(heures).zfill(2)
    minutes = str(minutes).zfill(2)
    return f"{heures}:{minutes}{am_pm}"


## Error handling

# check si on nous a transmis 1 arguements (notre heure)
if len(sys.argv) != 2:
    print("erreur : Pas le bon nombre d'arguments veuillez saisir une heure au format 24h, \"23:59\"")
    sys.exit()

# check format de l'argument 
ctrl_format(sys.argv[1])

# check que l'argument soit bien une heure au format 24h
ctrl_heure_exist(sys.argv[1])
 
                 
## Parsing

heures = int(sys.argv[1][:2])
minutes = int(sys.argv[1][3:])



## Resolution

heures_converti, am_pm = convertisseur_24_12(heures)

resultat = heure_format_12(heures_converti, minutes, am_pm)


## Display

print(resultat)
