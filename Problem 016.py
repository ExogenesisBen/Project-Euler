x=2**1000
y=str(x)
z=len(y)

n=0
m=0
list1 = []
total=0

while n < z:
    list1 += y[n]
    n+=1

while m<z:
    total += int(list1[m])
    m+=1

print total
