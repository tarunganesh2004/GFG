# K largest Elements

def k_largest_elements(arr, k):
    # return sorted(arr, reverse=True)[:k] # O(nlogn), single line
    arr.sort(reverse=True)
    return arr[:k]

# using min heap
def k_largest(arr,k):
    import heapq
    heap = []
    for i in arr:
        if len(heap) < k:
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
    return heap[::-1]

arr = [12,5,787,1,23]
k = 2
print(k_largest_elements(arr, k))
print(k_largest(arr, k))