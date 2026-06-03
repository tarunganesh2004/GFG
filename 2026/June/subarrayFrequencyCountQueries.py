arr=[1,2,1,3,1,2,3]
queries=[[0,4,1],[2,5,2],[1,6,3],[0,6,5]]

def freqInRangeBrute(arr,queries):
    def count(t,val):
        c=0
        for num in t:
            if num==val:
                c+=1
        return c
    
    res=[]
    for query in queries:
        i,j,val=query[0],query[1],query[2]

        sub=arr[i:j+1]
        res.append(count(sub,val))
    
    return res 

def optimal(arr,queries):
    from collections import defaultdict

    # store positions
    pos=defaultdict(list)
    res=[]
    for i,num in enumerate(arr):
        pos[num].append(i)

    for query in queries:
        l, r, val = query[0], query[1], query[2]
        count=0
        for p in pos[val]: # this is normal search, 

            if l<=p<=r:
                count+=1
        res.append(count)
    return res

# further optimized approach can be done using binary search to find the starting and ending positions of the valid occurences
def optimizedBinarySearch(arr,queries):
    from bisect import bisect_left,bisect_right
    from collections import defaultdict
    pos = defaultdict(list)

    # store positions
    for i, num in enumerate(arr):
        pos[num].append(i)

    res = []

    for l, r, val in queries:

        positions = pos[val]

        left = bisect_left(positions, l)

        right = bisect_right(positions, r)

        res.append(right - left)

    return res

print(freqInRangeBrute(arr,queries))
print(optimal(arr,queries))
print(optimizedBinarySearch(arr,queries))
