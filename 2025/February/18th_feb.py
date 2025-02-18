# K closest points to origin

k=2
points=[[1,3],[-2,2],[5,8],[0,1]]

# bruteforce 
def bruteforce(points,k):
    points.sort(key=lambda x: x[0]**2 + x[1]**2)
    return points[:k]

# using min heap
def k_closest(points,k):
    import heapq
    heap=[]
    for i in points:
        dist = i[0]**2 + i[1]**2
        if len(heap) < k:
            heapq.heappush(heap, (-dist, i))
        else:
            if heap[0][0] < -dist:
                heapq.heappop(heap)
                heapq.heappush(heap, (-dist, i))

    return [i[1] for i in heap]

print(bruteforce(points,k))
print(k_closest(points,k))