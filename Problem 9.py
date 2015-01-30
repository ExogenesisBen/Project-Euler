def triplet(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    return False

def findAnswer():
    for b in range (0,500):
        a = 0
        while a < b:
            if 2*a*b - 2000 *a - 2000*b + 1000000 == 0:
                c = 1000 - a - b
                print ("Solution found: ")
                print (a,b,c)
                return a*b*c
            a += 1
    return -1

print (findAnswer())

