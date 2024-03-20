def jeudupendu(mot):
    nb_erreur = 3
    a = ["_"]*len(mot)
    faute = ""
    while nb_erreur > 0:
        print("Devine mon mot:",end=" ")
        print(" ".join(a))
        print("Tu as droit a",nb_erreur,"erreurs","(",faute,")")
        lettre = input()
        i = 0
        nb = 0
        while i < len(mot):
            if mot[i] == lettre:
                nb = nb + 1
                a.insert(i,lettre)
                a.pop(i+1)
            i = i + 1
        if nb != 0:
            print("Il y a",nb,lettre)
            if a == list(mot):
                nb_erreur = -1
        else:
            print("Il n'y a pas de",lettre)
            faute = faute + " " + lettre
            nb_erreur -= 1
    if a == list(mot):
        print("Tu as gagné")
    else:
        print("Tu as perdu\nLe mot est",mot)
jeudupendu("bonjour")
            

        

         