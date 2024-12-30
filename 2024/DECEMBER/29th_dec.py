# Intersection of two arrays with duplicate elements

a=[1,2,1,3,1]
b=[3,1,3,4,1]

def intersection(a,b):
    #Using set
    sa=set(a)
    r=set()
    for i in b:
        if i in sa:
            r.add(i)
    return list(r)
    # return list(set(a)&set(b))

print(intersection(a,b))