# # Nearly sorted
# Given an array arr[], where each element is at most k away from its target position, you need to sort the array optimally.
# Note: You need to change the given array arr[] in place.

import heapq
arr=[6,5,3,2,8,10,9]
k=3

def nearlySorted(arr,k):
    heap=arr[:k+1]
    heapq.heapify(heap)

    i=0
    cur=k+1

    while cur<len(arr):
        popped=heapq.heappop(heap)
        arr[i]=popped

        heapq.heappush(heap,arr[cur])
        cur+=1
        i+=1
    
    while heap:
        cur=heapq.heappop(heap)
        arr[i]=cur
        i+=1

    return arr

print(nearlySorted(arr,k))