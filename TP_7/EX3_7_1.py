# Tri insertion
def tri_insertion(liste):
    liste_triee = []
    liste_triee.append(liste[0])
    for i in range (1,len(liste)):
        j = 0
        while j < len(liste_triee) and liste_triee[j] < liste[i] :
            j += 1
        liste_triee.insert(j,liste[i])
    return liste_triee

# Tri selection
def valeurmini(L):
    mini = L[0]
    for i in L:
        if i<mini:
            mini = i
    return mini
def tri_selection(L):
    lt = []
    while len(L) > 0:
        mini = valeurmini(L)
        L.remove(mini)
        lt.append(mini)
    return lt
def tri_selection2(L):
    lcopie = list(L)
    lt = []
    for i in range(0,len[L]):
        lt.append(lcopie.pop(lcopie.index(min(lcopie))))
    return lt

# Tri à bulle
def tri_à_bulle(l):
    lcopie = list(l)
    print(lcopie)
    n = len(lcopie)
    for i in range(n-1):
        for j in range(n-i-1): # n-i car la plus grande valeur remonte en haut
            if lcopie[j] > lcopie[j+1]:
                print("échange de",lcopie[j],"et",lcopie[j+1])
                temp = lcopie[j]
                lcopie[j] = lcopie[j+1]
                lcopie[j+1] = temp
        print(lcopie)
    return lcopie
print(tri_à_bulle([7,1,6,4,2,5,9,3,8,10]))
        
            

    
            
            
