# Find Only Repetitive Element from 1 to n-1

arr=[1,3,2,3,4]

# brute force
def brute_force(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                return arr[i]
    return -1

# using map 
def using_map(arr):
    # n=len(arr)
    map={}
    for num in arr:
        if num in map:
            return num
        else:
            map[num]=1
    return -1

# O(1) space and O(n) time complexity
def optimized(arr):
    for i in range(len(arr)):
        e=abs(arr[i])
        if arr[e]<0:
            return e
        arr[e]*=-1
    return 0


print(brute_force(arr))  # Output: 3
print(using_map(arr))  # Output: 3

print(optimized(arr))  # Output: 3