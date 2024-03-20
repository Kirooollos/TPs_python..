# rechercher dans une liste

def minimum(liste): # renvoyer minimum
    i = 0
    mini = liste[0]
    while i < len(liste):
        if liste[i] <= mini:
            mini = liste[i]
        i += 1
    return mini

def maximum(liste):
    return max(liste)

def contient(liste,elem): # vérifier si element est dans liste
    i = 0
    x = False
    while i<len(liste) and x == False:
        if elem == liste[i]:
            x = True
        i += 1
    return x

def minimum2(liste): #renvoyer la deuxieme elem le plus petit
    copy = list(liste)
    mini = minimum(copy)
    copy.remove(mini)
    mini2 = minimum(copy)
    return mini2

# Températures
def proche_zero(liste_entiers):
    ordre = 0
    positive =False
    negative = False
    while ordre < len(liste_entiers):
        if liste_entiers[ordre] >0:
            positive = True
        if liste_entiers[ordre] <0:
            negative = True
        ordre += 1
    if positive and negative:
        liste_positive = []
        liste_negative = []
        i = 0
        while i < len(liste_entiers):
            if liste_entiers[i] >= 0:
                liste_positive.append(liste_entiers[i])
            elif liste_entiers[i] <= 0:
                liste_negative.append(liste_entiers[i])
            i += 1
        mini = minimum(liste_positive)
        maxi = maximum(liste_negative)
        if mini + maxi > 0:
            resultat = maxi
        else:
            resultat = mini
        return resultat
    elif positive and not negative:
        return minimum(liste_entiers)
    elif not positive and negative:
        return maximum(liste_entiers)
    elif not positive and not negative:
        return 0

# Duels de chevaux de course
def plus_proche(liste):
    i = 0
    mini = abs(liste[1]-liste[0])
    while i < len(liste):
        n = len(liste)-1
        while n > i:
            if abs(liste[i]-liste[n]) <= mini:
                mini = abs(liste[i]-liste[n])
                cheval1 = i
                cheval2 = n
            n -= 1
        i += 1
    return cheval1,cheval2,mini
print(plus_proche([15,2,42,26,30,]))
    



        