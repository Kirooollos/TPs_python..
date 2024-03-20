from random import randint
from turtle import *

def carré(): 
    color("red")
    cote = 4
    speed(2)
    while cote > 0:
        forward(100)
        left(90)
        cote = cote - 1  
    done()


def carré_bis():
    color("red")
    cote = 4
    speed(2)
    up()
    goto(-50,20)
    down()
    while cote > 0:
        forward(100)
        right(90)
        cote = cote - 1
    done()


def triangle_équilatéral():
    color("pink")
    cote = 3
    speed(1)
    while cote > 0:
        right(120)
        forward(100)
        cote = cote - 1
    right(120)
    done()
    

def pavage_carre():
    color("pink")
    speed(10)
    up()
    goto(-200,200)
    down()
    ligne = 1
    while ligne <= 4:
        nc = 1
        while nc <= 8:
            i = 1
            while i <= 4:
                forward(50)
                right(90)
                i = i + 1
            up()
            forward(60)
            down()
            nc = nc + 1
        up()
        goto(-200,(200 - ligne * 70))
        down()
        ligne = ligne + 1
        
        
def carre_triangle_alterne():
    color("pink")
    up()
    goto(-200,200)
    down()
    a=int(input("donner un nb de figures: "))
    i=1
    while i<=a:
        j=1
        if i%2 !=0:
            while j<=4:
                forward(50)
                right(90)
                j=j+1   
        else:
            while j<=3:
                forward(50)
                right(120)
                j = j + 1
        up()
        forward(60)
        down()
        i = i + 1
    done()


def rosace(x,y,nb,r,t1,tp):
    from random import randint
    colormode(225)
    m = 1
    speed(11)
    up()
    goto(x,y)
    down()
    while m <= tp:
        n = 1
        while n <= t1:
            color(randint(0,100))
            i = 1
            while i<=nb: 
                circle(r)
                right(360/nb)
                i = i + 1
            n += 1
            up()
            forward(2*r + 20)
            down()
        up()
        goto(x,y-(m*4*r))
        down()
        m += 1
    done()
rosace(-100,0,8,10,4,3)



    
    

    
    


        
        
        