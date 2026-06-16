# Construct List using XOR Queries

q=5
queries = [[0, 6], [0, 3], [0, 2], [1, 4], [1, 5]]

def constructList(queries):
    res=[]
    xor_val=0
    for t,x in queries:
        if t==0:
            res.append(x^xor_val)
        else:
            xor_val^=x
    
    ans=[xor_val^num for num in res]
    ans.append(xor_val)
    return sorted(ans)

print(constructList(queries))