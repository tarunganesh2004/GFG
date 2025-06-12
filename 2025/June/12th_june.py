# K Closest Elements 

arr=[1,3,4,10,12]
k=2
x=4

def printKClosest(arr,k,x):
    import heapq 
    heap=[]
    for i in arr:
        if i==x:
            # skip 
            continue
        heapq.heappush(heap, (abs(i-x), -i))
    result = []
    while (heap and k):
        _,val= heapq.heappop(heap)
        result.append(-val)
        k -= 1
    return result

print(printKClosest(arr, k, x))  # Output: [3, 1]