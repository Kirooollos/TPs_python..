#1
def pg():
    import random
    fr = {"chien":"dog",
          "chat":"cat",
          "lapin":"rabbit",
          "tortue":"turtle",}
    nb_joueurs = int(input("nb_joueurs: "))
    dico={}
    # nom des joueurs
    for cle in range(nb_joueurs):
        nom=input("nom du joueur: ")
        dico[nom]=0
    # choix des mots
    nb_tours = int(input("nb de tours le la partie: "))
    choix_mots=[]
    liste =list(fr.keys())
    while nb_tours>=1:
        x = liste[random.randint(0,len(liste)-1)]
        choix_mots.append(x)
        liste.remove(x)
        nb_tours -= 1
    # jeu
    
    for j in dico:
        nb_mots=0
        print("tour de",j)
        for i in choix_mots:
            print("traduction de",i,":",end="")
            devine = input()
            if devine == fr[i]:
                dico[j] += 1
            nb_mots += 1
    for i in dico:
        dico[i]= round(dico[i]/nb_mots*100)
    
    return dico

#5
def multi_joueurs(dico_scores):
    maxi = 0
    for i in dico_scores:
        if dico_scores[i] > maxi:
            maxi = dico_scores[i]
            nom = i
    return nom,maxi

#6        
def jeu_principal(dict_scores):
    liste_nom = []
    liste_score = []
    for i in range (0,3):
        nom = multi_joueurs(dict_scores)[0]
        score = multi_joueurs(dict_scores)[1]
        liste_nom.append(nom)
        liste_score.append(score)
        del dict_scores[nom]
    j = 0
    while j<=1:
        score1 = liste_score[j]
        score2 = liste_score[j+1]
        if score1 == score2:
            if liste_nom[j][0]>liste_nom[j+1][0]:
                liste_nom.insert(j+2,liste_nom[j])
                liste_nom.pop(j)
        j += 1
    ordre = 1
    k = 0
    for m in range(0,3):
        if k>=1:
            if liste_score[k]!=liste_score[k-1]:
                ordre += 1
        print(ordre,". ",liste_nom[k],"  ",liste_score[k],"\%",sep="")
        k += 1
jeu_principal({"trung":40,
               "kiro":30,
               "haha":15,
               "nara":40,
               "gha":47})      
        
    