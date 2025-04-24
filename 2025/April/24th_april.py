# Unique Number III

arr=[1,10,1,1]

# using map 
def getSingle(arr):
    from collections import Counter
    count = Counter(arr)
    for k,v in count.items():
        if v == 1:
            return k
    return -1

print(getSingle(arr))  # Output: 10