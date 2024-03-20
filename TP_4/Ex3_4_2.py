#La bosse des maths


def valeur_abs(x):
    return abs(x)
 

def signe_different(x,y):
    signe = True
    if x*y > 0:
        signe = True
    else:
        signe = False
    return signe

def f(x):
    return 3*x**2 + 2*x +3

#Polynome

def nb_racines(a,b,c):
    delta = b**2 - 4*a*c
    if delta > 0:
        nb = 2
    elif delta == 0:
        nb = 1
    else:
        nb = 0
    return nb


def resolution(a,b,c):
    from math import sqrt
    delta = b**2 - 4*a*c
    if nb_racines(a,b,c) == 2:
        print((-b + sqrt(delta))/(2*a),(-b - sqrt(delta))/(2*a),sep=";")
    elif nb_racines(a,b,c) == 1:
        print(-b / (2*a))
    else:
        print("none")
    print(nb_racines(a,b,c))
import random
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
resolution(a,b,c)

    
