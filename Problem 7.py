import time

n = 200000

start = time.time() #-------------------------------------

numbers = set(range(n, 1, -1))

primes = []
while numbers:
    p = numbers.pop() # takes off the last element of numbers
    primes.append(p)

    # return set numbers after removing elements found in numbers
    numbers.difference_update(set(range(p*2, n+1, p)))

elapsed = time.time() - start #---------------------------
print  "Time taken is:", elapsed


primes.sort()
print primes[10000]
