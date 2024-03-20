def est_premier(a):
    s = 0
    for i in range(1,a+1):
        if a%i == 0:
            s += 1
    if s==2:
        premier = True
    else:
        premier = False
    return premier

def plus_grand_diviseur_premier(n):
    i = 1
    while i <= n:
        if est_premier(i)==True:
            p = n % i
            if p == 0:
                maxi = i
        i += 1
    return maxi

def pgcd(a,b):
    if a > b:
        c = a
        a = b
        b = c
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b
print(pgcd(20,50))
        
        