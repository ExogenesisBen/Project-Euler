def multiples(limit,x,y):
    total = 0
    z = 0
    while z < limit:
        if z%x == 0 or z%y == 0:
            total += z
        z+=1
    print total


multiples(1000,3,5)
