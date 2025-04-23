# Unique Number II

arr=[1,2,3,2,1,4]

def uniqueNumbers(arr):
    from collections import Counter
    count = Counter(arr)
    res=[]
    for k,v in count.items():
        if v == 1:
            res.append(k)
    return sorted(res)

print(uniqueNumbers(arr))  # Output: [3, 4]