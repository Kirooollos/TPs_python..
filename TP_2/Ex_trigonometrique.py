from math import *
def trigo_1():
    h = float(input("l'hypoténuse: "))
    a = float(input("l'angle(en radians): "))
    b = cos(a) * h
    c = sin(a) * h
    print("les deux cotes sont:",b,",",c)

def trigo_1b():
    h = float(input("l'hypoténuse: "))
    a = float(input("l'angle(en radians): "))
    b = cos(a) * h
    c = sin(a) * h
    if h**2 == b**2 + c**2:
        print("vrai")
    else:
        print("faux")

def trigo_2():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    delta = b**2 - 4*a*c
    while delta < 0:
        a = float(input("choisir autre a = "))
        b = float(input("choisir autre b = "))
        c = float(input("choisir autre c = ")) 
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        if x1 != x2:
            print("les racines du polynome ax^2 + x + 1 sont:",x1,"et",x2)
        else:
            print("les racines du polynome ax^2 + x + 1:",x1)
    