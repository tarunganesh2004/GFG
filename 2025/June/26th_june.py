# Game with String

s="abbccc"
k=2

def minValue(s,k):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    
    l=list(d.values())  # noqa: E741
    for j in range(k):
        x=l.index(max(l))
        l[x]=max(l)-1
    a=0
    for i in l:
        a+=i**2
    return a

print(minValue(s,k)) 