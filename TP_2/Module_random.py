import random
def ver_1():    
    x = random.randint(1,4)
    print(x)
    
def ver_2():
    a = int(input("a = "))
    b = int(input("b = "))
    if a < b:
        print(random.randint(a,b))
ver_2()