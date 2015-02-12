#pal = palindromic

n = 1

def pal(n):
    forwards = str(n)
    backwards = forwards[::-1]
    return forwards == backwards

def checker():
    longest = 0
    largest = 0
    for m in range(1000):
        for n in range(1000):
            p = m*n
            if pal(p) and p > largest:
                largest = p
    p = largest
    print largest


checker()
