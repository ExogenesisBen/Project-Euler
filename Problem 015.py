def route_num(size):
    #makes an array of grid size
    L = [1] * size

    #loops for size of grid
    for i in range(size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[size - 1]

print route_num(20)

# I made a solution for this problem a while ago which was perfectly okay
# but not too efficient. A long time later I accidently came across this
# very elegant solution. The mathematics behind it, along with the code,
# can be found here:
# http://code.jasonbhill.com/python/project-euler-problem-15/
