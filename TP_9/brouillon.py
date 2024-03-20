notes_groupe = [
    {"nom": "lambert", "note":{"physique":12, "info":11}},
    {"nom": "ment", "note": {"maths":13.5, "info": 18, "sport": 17}}
]

def moyenne_etudiant(etudiant):
    lenth = 0
    for i in etudiant["note"]:
        lenth += 1
    somme = 0
    for j in etudiant["note"]:
        somme += etudiant["note"][j]
    moyenne = somme/lenth
    nom = etudiant["nom"]
    return nom,moyenne

def meilleur(notes_groupe):
    dicte = {}
    for i in range (0,len(notes_groupe)):
        nom,moyenne = moyenne_etudiant(notes_groupe[i])
        dicte[nom]=moyenne
    maxi = 0
    for j in dicte:
        if dicte[j] > maxi:
            maxi = dicte[j]
            nom_maxi = j
    return maxi,nom_maxi

