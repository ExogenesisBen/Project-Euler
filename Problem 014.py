def collatzSequenceLength(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        length += 1
    return length
    
start = 1
greatest = 0

while start < 1000000:
    current = collatzSequenceLength(start)
    if current > greatest:
        greatest = current
        greatestStart = start
    start += 1
    
print (greatestStart)
print (greatest)

#Not very efficient, to be improved
