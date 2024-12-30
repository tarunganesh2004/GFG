# Merge Without Extra space

a=[2,4,7,10]
b=[2,3]

def mergeArrays(a,b):
    merged=sorted(a+b)
    a[:]=merged[:len(a)]
    b[:]=merged[len(a):]

mergeArrays(a,b)
print(a,b)