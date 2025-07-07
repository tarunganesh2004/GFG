# Maximum Sum Combination

a=[3,2]
b=[1,4]
k=2

def maxSumCombination(a, b, k):
    import heapq
    a.sort(reverse=True)
    b.sort(reverse=True)

    heap=[]
    vis=set()

    heapq.heappush(heap,(-(a[0]+b[0]),0,0))
    vis.add((0,0))

    res=[]
    for _ in range(k):
        cur_sum,i,j= heapq.heappop(heap)
        res.append(-cur_sum)

        # next pair (i+1,j)
        if i+1 < len(a) and (i+1, j) not in vis:
            heapq.heappush(heap, (-(a[i+1] + b[j]), i+1, j))
            vis.add((i+1, j))
        
        # next pair (i,j+1)
        if j+1<len(b) and (i,j+1) not in vis:
            heapq.heappush(heap, (-(a[i] + b[j+1]), i, j+1))
            vis.add((i, j+1))
    return res

print(maxSumCombination(a, b, k))