from math import *

def makeF(n):
    r=1
    total1=1
    while r-1<n:
        total1*=r
        r+=1
    return total1

def getF(n):
    m=0
    x=str(makeF(n))
    print x
    total=0
    while m+1 < len(x):
        total +=int(x[m])
        m+=1
    print total, "is the answer!"

n=100
getF(n)
