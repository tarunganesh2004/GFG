# Longest Increasing Subsequence

arr=[5,8,3,7,9,1]

# using dp
def bruteForce(arr):
    n=len(arr)
    dp=[1]*n
    for i in range(1,n):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)

# using binary search
def optimized(arr):
    from bisect import bisect_left
    n=len(arr)
    dp=[0]*n
    length=0
    for num in arr:
        i=bisect_left(dp,num,0,length)
        dp[i]=num
        if i==length:
            length+=1
    return length

# using sortedlist
def optimized2(arr):
    from sortedcontainers import SortedList
    sl=SortedList()
    for num in arr:
        index=sl.bisect_left(num)
        if index==len(sl):
            sl.add(num)
        else:
            sl[index]=num
    return len(sl)

# using map 
def optimized3(arr):
    from sortedcontainers import SortedDict
    sd=SortedDict()
    for num in arr:
        sd[num]=sd.get(num,0)+1
        if num-1 in sd:
            sd[num]=max(sd[num],sd[num-1]+1)
    return max(sd.values())

print(bruteForce(arr)) # 3
print(optimized(arr)) # 3
print(optimized2(arr)) # 3
print(optimized3(arr)) # 3