from math import *

    
def makeF(n):
    return reduce(lambda y,x:y*x,range(1,n+1))

def sumOFlist(number):
    return reduce(lambda y,x:int(y)+int(x),number)


n=100

number = str(makeF(n))
print "The answer is: ", sumOFlist(number)
