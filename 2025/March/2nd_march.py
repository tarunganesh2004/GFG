# K Sized Subarray Maximum

from collections import deque


arr=[1,2,3,1,4,5,2,3,6]
k=3

# brute force
def bruteForce(arr,k):
    res=[]
    for i in range(len(arr)-k+1):
        res.append(max(arr[i:i+k]))
    return res

# optimized approach
def maxOfSubarray(arr,k):
    q=deque()
    res=[]
    for i in range(len(arr)):
        while q and arr[i]>arr[q[-1]]:
            q.pop()
        q.append(i)
        if q[0]==i-k:
            q.popleft()
        if i>=k-1:
            res.append(arr[q[0]])
    return res

print(bruteForce(arr,k))
print(maxOfSubarray(arr,k))