
def trois_des():
    n1 = int(input("premier nombre: "))
    n2 = int(input("deuxième nombre: "))
    n3 = int(input("troisième nombre: "))
    if 1 <= n1 <= 6 and 1 <= n2 <= 6 and 1 <= n3 <= 6:
    
        if n1 >= n2:
            de1 = n1
            de2 = n2
        else:
            de1 = n2
            de2 = n1
        if n3 >= de1:
            de3 = de2
            de2 = de1
            de1 = n3
        elif n3 >= de2:
            de3 = de2
            de2 = n3
        else:
            de3 = n3
        print(de1, de2, de3)
        if (de1, de2, de3) == (4, 2, 1):
            print("gagné")
        else:
            print("perdu")

