from math import *

fib=[]
a=-1
b=1
def fibonacci(a,b):
    if a+b>=4000000:
        return
    else:
        a,b = b,a+b
        fib.append(b)
        fibonacci(a,b)
    return fib

fib1=fibonacci(a,b)

#eC is evenChecker

def eC(fib1):
    n=0
    total=0
    while n < len(fib1):
        if fib1[n] %2 == 0:
            total+=fib1[n]
        n+=1
    print total


eC(fib)
