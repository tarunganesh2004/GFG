# Union of two sorted arrays with distinct elements

a=[1,2,3,4,5]
b=[1,2,3,6,7]

def union(a,b):
    s=set()

    for i in a:
        s.add(i)

    for i in b:
        s.add(i)

    l=[]
    for k in s:
        l.append(k)
    print(l)

union(a,b)