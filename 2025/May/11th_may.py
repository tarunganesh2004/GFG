# Kth Largest Sum Contiguous Subarray

arr=[3,2,1]
k=2


# brute force
def kthLargestSum(arr,k):
    n=len(arr)
    sums=[]

    for i in range(n):
        sm=0
        for j in range(i,n):
            sm+=arr[j]
            sums.append(sm)

    sums.sort()
    return sums[-k]

# Optimized using heap
def optimized(arr,k):
    import heapq
    res=[]
    for i in range(len(arr)):
        sm=0
        for j in range(i,len(arr)):
            sm+=arr[j]
            res.append(sm)
    heapq.heapify(res)
    return heapq.nlargest(k,res)[-1]

def anotherWay(arr,k):
    import heapq
    min_heap = []
    for i in range(len(arr)):
        sm=0
        for j in range(i,len(arr)):
            sm+=arr[j]
            # push the tuple of (sum,start_idx,end_idx) into the heap
            if len(min_heap) < k:
                heapq.heappush(min_heap, (sm, i, j))
            else:
                # if the heap is full and the current sum is greater than the smallest in the heap
                if sm > min_heap[0][0]:
                    # heapq.heappop(min_heap)
                    heapq.heappushpop(min_heap, (sm, i, j))
        
        kth_sum,start,end= heapq.heappop(min_heap)
        return kth_sum,arr[start:end+1]

print(kthLargestSum(arr,k)) 
print(optimized(arr,k)) 
print(anotherWay(arr,k)) 