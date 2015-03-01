#Euler 48

mod = 10000000000
total = 0

for i in range(1,1001):
	powerOfSelf = (i**i) % mod
	total = ((total + powerOfSelf) % mod)

print "The answer is: " + str(total)