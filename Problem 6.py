#y is max number ie 10 or 100
#x is to the power ie 2

#sOP is sum of powers

def sOP(x,y):
    total=0
    n=1
    while n <= y:
        sum=n**x
        n=n+1
        total +=sum
    return total

#pOSum is powers of sum

def pOS(x,y):
    total=0
    n=1
    while n <= y:
        total +=n
        n=n+1
    grandtotal=total**x
    return grandtotal

w=sOP(2,100)
z=pOS(2,100)

final = z - w
print final
