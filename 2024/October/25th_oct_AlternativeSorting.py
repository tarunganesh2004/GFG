l=[7,1,2,3,4,5,6]
# o/p: 7,1,6,2,5,3,4

def convert(l):
    l.sort() # 1 2 3 4 5 6 7
    l.reverse() # 7 6 5 4 3 2 1
    r=[]
    n=len(l)
    for i in range(n//2): # 0 1 2 
        r.append(l[i])
        r.append(l[n-i-1])

    if n%2!=0:
        r.append(l[n//2])

    return r
r=convert(l)
print(r)