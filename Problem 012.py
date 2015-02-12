from math import *

def numOfDivisors(n):
    totalNum = 2
    i = 1
    root = sqrt(n)
    while i <= root:
        if n % i == 0:
            totalNum += 2
        i += 1
    return totalNum

def TriangleNums():
    i = 1
    n = 0
    while True:
        n += i  # n is always a triangle number as adding on the next i every time
        if numOfDivisors(n) > 500:
            return n
        i += 1

print TriangleNums()
