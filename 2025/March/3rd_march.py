# # Longest Bounded Difference Subarray

# Given an array of positive integers arr[] and a non-negative integer x, the task is to find the longest sub-array where the absolute difference between any two elements is not greater than x.
# If multiple such subarrays exist, return the one that starts at the smallest index.

# brute force



arr=[8,4,2,6,7]
x=4

def bruteForce(arr,x): # O(n^3)
    res=[]
    n=len(arr)
    max_len=0
    for i in range(n):
        for j in range(i,n):
            subarr=arr[i:j+1]
            if max(subarr)-min(subarr)<=x:
                if len(subarr)>max_len:
                    max_len=len(subarr)
                    res=subarr
    return res

# using sortedlist and sliding window
def optimized(arr,x):
    from sortedcontainers import SortedList
    sl=SortedList()
    i=0
    max_len=0
    res=[]

    for j in range(len(arr)):
        sl.add(arr[j])
        while sl[-1]-sl[0]>x: # type: ignore
            sl.remove(arr[i])
            i+=1
        if j-i+1>max_len:
            max_len=j-i+1
            res=arr[i:j+1]
    return res

print(bruteForce(arr,x))
print(optimized(arr,x))