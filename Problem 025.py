from math import *

fib0=[]
fib1=[]
fib2=[]
fib3=[]
fib4=[]
fib5=[]
n=0

def fibonacci(a,b,n):
    while n < 900:
        if len(fib0) == 900:
            return fib0
        else:
            a,b = b,a+b
            fib0.append(b)
            fibonacci(a,b,n)
            n+=1
        return fib0

def fibonacci1(x,y,n):
    while n < 900:
        if len(fib1) == 900:
            return fib1
        else:
            x,y = y,x+y
            fib1.append(y)
            fibonacci1(x,y,n)
            n+=1
        return fib1

def fibonacci2(z,w,n):
    while n < 900:
        if len(fib2) == 900:
            return fib2
        else:
            z,w = w,z+w
            fib2.append(w)
            fibonacci2(z,w,n)
            n+=1
        return fib2

def fibonacci3(e,f,n):
    while n < 900:
        if len(fib3) == 900:
            return fib3
        else:
            e,f = f,e+f
            fib3.append(f)
            fibonacci3(e,f,n)
            n+=1
        return fib3

def fibonacci4(g,h,n):
    while n < 900:
        if len(fib4) == 900:
            return fib4
        else:
            g,h = h,g+h
            fib4.append(h)
            fibonacci4(g,h,n)
            n+=1
        return fib4
    
def fibonacci5(i,j,n):
    while n < 900:
        if len(fib5) == 900:
            return fib5
        else:
            i,j = j,i+j
            fib5.append(j)
            fibonacci5(i,j,n)
            n+=1
        return fib5

    
a=-1
b=1
fibA = fibonacci(a,b,n)

x=fibA[-2]
y=fibA[-1]
fibB = fibonacci1(x,y,n)

z=fibB[-2]
w=fibB[-1]
fibC = fibonacci2(z,w,n)

e=fibC[-2]
f=fibC[-1]
fibD = fibonacci3(e,f,n)

g=fibD[-2]
h=fibD[-1]
fibE = fibonacci4(g,h,n)

i=fibE[-2]
j=fibE[-1]
fibF = fibonacci5(i,j,n)


def fibcheck(fibF):
    m=0
    while m<400:
        if len(str(fibF[m])) > 999:
            #print fibF[m-1]
            print "Answer is:", m +900*5
            return
        m+=1

fibcheck(fibF)
