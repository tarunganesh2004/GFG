# Union of arrays with Duplicates

a=[1,2,3,4,5]
b=[1,2,3]

def union(a,b):
    # Using set
    # s=set()
    # for i in a:
    #     s.add(i)
    # for i in b:
    #     s.add(i)
    return len(list(set(a+b)))

print(union(a,b))