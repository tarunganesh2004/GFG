# Triplet Family

l=[1,2,3,4,5]

def twoSum(l,key):
    i,j=0,len(l)-1
    while i<j:
        if l[i]+l[j]==key:
            return True
        elif l[i]+l[j]<key:
            i+=1
        else:
            j-=1
    return False


def findTriplet(l):
    n=len(l)
    l.sort()
    for i in l:
        if twoSum(l,i):
            return True
    return False

print(findTriplet(l))