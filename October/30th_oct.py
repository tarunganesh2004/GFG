# Pairs with difference k

l=[1,5,3,4,2]
k=3

def count_pairs(l,k):
    map={}
    n=len(l)
    count=0

    for i in range(n):
        if l[i] in map:
            map[l[i]]+=1
        else:
            map[l[i]]=1

    for a in l:
        if a+k in map:
            count+=map[a+k]
        if a-k in map:
            count+=map[a-k]

    return count//2

print(count_pairs(l,k)) # 2