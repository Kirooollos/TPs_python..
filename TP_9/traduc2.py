#Exercice2


import random
def traduire(di,mot):
    return di[mot]
def jouerUnMot(di):
    liste =list(di.keys())
    x = liste[random.randint(0,len(liste)-1)]
    print("traduction de",x,":", end=" ")
    reponse = input()
    if reponse == di[x]:
        res="succes"
    else:
        res="echec"
    return res, reponse==di[x]

#print(jouerUnMot(fr))
def pg1():
    fr = {"chien":"dog",
      "chat":"cat",
      "carafe":"bottle"}
    boo = True
    tours = 0
    points = 0
    while boo == True:
        if jouerUnMot(fr)[1]:
            points += 1
        tours += 1
        a = input("continuer/arreter?")
        if a == "arreter":
            boo = False
    #print(points,"/",tours)

        
    
    