# le jeu de base
import random

def ver_1():
    a = random.randint(0,100)
    b = int(input("deviner le nombre: "))
    while b != a:
        if b > a:
            print("trop grand")
        else:
            print("trop petit")
        b = int(input("deviner un autre nombre: "))
    print("gagné")


def ver_2():
    a = random.randint(0,100)
    b = int(input("deviner le nombre: "))
    max = 100
    min = 0
    while b != a:
        if b > a:
            print("trop grand")
            max = b - 1
        else:
            print("trop petit")
            min = b + 1
        print("devine nombre entre",min ,"et",max,":" )
        b = int(input())
    print("gagné")


def ver_3():
    a = 50
    b = int(input("deviner le nombre: "))
    max = 100
    min = 0
    n = 4
    resultat = True
    while b != a and resultat:
        while n > 0:
            if b > a:
                print("trop grand")
                max = b - 1
            elif b < a:
                print("trop petit")
                min = b + 1
            print("devine nombre entre",min ,"et",max,":",end=" ")
            b = int(input())
            n -= 1
        resultat = False
    if resultat:
        print("gagné après",5-n,"essaies")
    else:
        print("perdu")
ver_3()

        


    
            