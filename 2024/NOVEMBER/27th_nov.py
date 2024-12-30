# Smallest positive missing number
l=[2,-3,4,1,1,7]
def smallestPositive(l):
    n=len(l)
    s=set(l)

    smallest=1

    while smallest in s:
        smallest+=1

    return smallest

print(smallestPositive(l))