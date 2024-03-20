def triangle(n,c1,c2):
    if c1<=c2:
        l = 1
        c = c1 
        while l <= n:
            i = 1
            while i <= l:
                print(c,end=" ")
                if c == c2:
                    c = c1
                else:
                    c = chr(ord(c) + 1)
                i += 1
            print()
            l += 1
triangle(5,"A","H") 