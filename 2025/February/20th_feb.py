# Find Median in a Stream

arr=[5,15,1,3,2,8]
# output: [5.0,15.0,5.0,4.0,3.0,4.0]

import heapq  # noqa: E402
def getMedianBrute(arr):
    # brute force
    # time complexity: O(n^2)
    res=[]
    for i in range(1,len(arr)+1):
        l=arr[:i]  # noqa: E741
        l.sort()
        if len(l)%2==0:
            res.append((l[len(l)//2]+l[len(l)//2-1])/2)
        else:
            res.append(l[len(l)//2])
    return res

# optimized approach
# using two heaps(min and max)
def getMedian(arr):
    # time complexity: O(nlogn)
    # space complexity: O(n)
    min_heap=[]
    max_heap=[]
    res=[]
    for i in arr:
        if not max_heap or i<=-max_heap[0]:
            heapq.heappush(max_heap,-i)
        else:
            heapq.heappush(min_heap,i)
        if len(max_heap)>len(min_heap)+1:
            heapq.heappush(min_heap,-heapq.heappop(max_heap))
        elif len(min_heap)>len(max_heap):
            heapq.heappush(max_heap,-heapq.heappop(min_heap))
        if len(max_heap)==len(min_heap):
            res.append((-max_heap[0]+min_heap[0])/2)
        else:
            res.append(-max_heap[0])
    return res

print(getMedianBrute(arr))
print(getMedian(arr))