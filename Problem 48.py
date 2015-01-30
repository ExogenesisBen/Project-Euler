n=1
total = 0

while n<=1000:
    total += n**n
    n+=1

print total % 10000000000
