# Smallest Positive Missing 

arr=[2,-3,4,1,1,7]

# brute force
def smallestMissingBrute(arr):
    s=set(arr)
    smallest=1
    while smallest in s:
        smallest += 1
    return smallest

# Optimal O(1) Space and O(n) Time Complexity
def smallestMissingOptimal(arr):
    n = len(arr)
    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
    
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
    return n + 1


print(smallestMissingBrute(arr))
print(smallestMissingOptimal(arr))