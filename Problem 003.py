from math import *

#pF is primefactors

def pF(n):  
    i = 2
    while i <= sqrt(n):
        if n%i==0:
            l = pF(n/i)
            l.append(i)
            return l
        i+=1
    print n
    return [n]
    


pF(600851475143)
