

def factorisation(n):
    return 1 if n==1 else n * factorisation(n-1)

def somme(n):
    return 1 if n==1 else n + somme(n-1)

def fibonacci(n):
    return 1 if n==0 or n==1 else fibonacci(n-2) + fibonacci(n-1)

from math import *
def ucln(a,b):
    if a>b:
        max = a - b
        while a % max != 0:
            max = abs(max - b)
        print(max)
    else:
        max = b - a
        while b % max != 0:
            max = abs(max - a)
        print(max)
ucln(15,5)
        