s="fooland"
k=2

def lexicographicallySmallest(s,k):
    n=len(s)

    if n>0 and (n&(n-1))==0:
        k//=2
    else:
        k*=2
    
    if k>=n:
        return -1

    res=[]
    for ch in s:
        while res and k>0 and res[-1]>ch:
            res.pop()
            k-=1
        res.append(ch)

    while k>0:
        res.pop()
        k-=1
    return ''.join(res)


print(lexicographicallySmallest(s,k))    