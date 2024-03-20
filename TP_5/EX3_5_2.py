#Chiffre de César
from re import A


def decale(lettre):
    a = chr(ord(lettre)+3)   
    return a
def cesar(mot):
    i = 0
    a = ""
    while i <= len(mot)-1:
        a = a + decale(mot[i])
        i += 1
    return a

#Chiffrement d'un mot
def position(lettre):
    if "a" <= lettre <= "z":
        a = ord(lettre) - ord("a") + 1
    elif "A" <= lettre <= "Z":
        a = ord(lettre) - ord("A") + 1
    else: 
        a = lettre
    return a
def chiffrement(mot):
    b = []
    i = 0
    while i<=len(mot)-1:
        b.append(str(position(mot[i])))
        i += 1
    a = "+".join(b)
    return a 

#chiffrement d'un texte
def chiffrementtexte(texte):
    b = []
    i = 0
    while i < len(texte):
        b.append(str(position(texte[i])))
        i += 1
        if position(texte[i]) == texte[i]:
            continue
    a = "+".join(b)
    return a


