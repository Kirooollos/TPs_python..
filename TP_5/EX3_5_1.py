#question 1
from re import A


def lundi(mot):
    a = mot + " " + mot
    return a


#question 2
def mardi(mot):
    if len(mot) % 2 == 0:
        a = (mot + "-" ) * 5 + mot
    else:
        a = (mot + ",") * 2 + mot
    return a


#question 3
def mercredi(mot):
    if len(mot)%2!=0:
        a = "impair"
    else:
        a = mot
    return a


#question 4
def jeudi(mot):
    a = mot*(len(mot)%3)
    return a 


#question 6
def vendredi(mot):
    l = list(mot)
    if "a"<=mot[0]<="z":
        l.pop(0)
    else:
        l.pop(-1)
    a = "".join(l)
    return a


#question 7
def samedi(mot):
    i = len(mot) - 1
    a = ""
    while i >= 0:
        a = a + mot[i]
        i -= 1
    return a

#question 8
def dimanche(mot):
    a =" ".join(list(mot))
    return a 

#question 5
def transforme(mot,num_jour):
    if num_jour == 1:
        a = lundi(mot)
    elif num_jour == 2:
        a = mardi(mot)
    elif num_jour == 3:
        a = mercredi(mot)
    elif num_jour == 4:
        a = jeudi(mot)
    elif num_jour == 5:
        a = vendredi(mot)
    elif num_jour == 6:
        a = samedi(mot)
    elif num_jour == 7:
        a = dimanche(mot)
    return a

          
         



