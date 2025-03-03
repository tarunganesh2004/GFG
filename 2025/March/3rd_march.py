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

# Another approach is to use deque and sliding window
def longestSubarray(arr,x):
    from collections import deque
    max_q=deque()
    min_q=deque()
    i=0
    max_len=0
    res=[]

    for j in range(len(arr)):
        while max_q and arr[j]>max_q[-1]:
            max_q.pop()
        max_q.append(arr[j])
        while min_q and arr[j]<min_q[-1]:
            min_q.pop()
        min_q.append(arr[j])

        while max_q[0]-min_q[0]>x:
            if max_q[0]==arr[i]:
                max_q.popleft()
            if min_q[0]==arr[i]:
                min_q.popleft()
            i+=1
        if j-i+1>max_len:
            max_len=j-i+1
            res=arr[i:j+1]

    return res

print(bruteForce(arr,x))
print(optimized(arr,x))

print(longestSubarray(arr,x))