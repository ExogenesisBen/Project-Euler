#eD is evenlyDivisible

def eD(n):
    x = 0
    for i in range(1, 21):
        if n % i == 0:
            x += 1
            if x == 20:
                return n
        else:
            return 1

        
def main():
    n = 2520
    x = 1
    while x == 1:
        smallest = eD(n)
        if smallest != 1:
            print smallest
            x = 0
        else:
            n += 2520


main()
