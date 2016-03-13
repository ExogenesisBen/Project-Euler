
n = 2000000

numbers = set(range(n, 1, -1))

primes = []
while numbers:
    p = numbers.pop()
    primes.append(p)
    numbers.difference_update(set(range(p*2, n+1, p)))

total = 0

index = 0

while index < len(primes):
    total += primes[index]
    index+=1

print total
