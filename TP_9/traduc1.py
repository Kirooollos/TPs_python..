#Exercice1

def ajouteMot(dfren,mfr,wen):
    dfren[mfr]=wen
    
def supprimeMot(di,mot):
    del di[mot]
    
def afficheDico(di):
    for i in di:
        print(i,"=",di[i])

def afficheDicoLettre(di,lettre):
    for i in di:
        if i[0]==lettre:
            print(i)
        
def afficheDicoLongueur(di,longueur):
    for i in di:
        if len(i)==longueur:
            print(i,"=",di[i])

#programme principal
fr = {"chien":"dog",
      "chat":"cat",
      "carafe":"bottle"}
ajouteMot(fr,"lapin","rabbit")
afficheDico(fr)

