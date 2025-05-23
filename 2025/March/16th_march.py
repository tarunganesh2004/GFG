# # Minimum Jumps

# You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

# For example:

# If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
# If arr[i] = 0, you cannot jump forward from that position.
# Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.

# Note:  Return -1 if you can't reach the end of the array.

arr=[1,3,5,8,9,2,6,7,6,8,9]

# recursion
def min_jumpsRecur(i,arr): # O(n^n)
    if i>=len(arr)-1:
        return 0
    if arr[i]==0:
        return float("inf")
    min_jumps=float("inf")
    for j in range(1,arr[i]+1):
        min_jumps=min(min_jumps,1+min_jumpsRecur(i+j,arr))
    return min_jumps

# using lru_cache
def min_jumpsMemoi(arr):
    from functools import lru_cache
    arr = tuple(arr)

    @lru_cache(None)
    def helper(i):
        if i>=len(arr)-1:
            return 0
        if arr[i]==0:
            return float("inf")
        min_jumps=float("inf")
        for j in range(1,arr[i]+1):
            min_jumps=min(min_jumps,1+helper(i+j))
        return min_jumps
    return helper(0)

# memoization
def min_jumpsMemoiAnother(i,arr, memo=None):
    if memo is None:
        memo={}
    if i>=len(arr)-1:
        return 0
    if arr[i]==0:
        return float("inf")
    if i in memo:
        return memo[i]
    min_jumps=float("inf")
    for j in range(1,arr[i]+1):
        min_jumps=min(min_jumps,1+min_jumpsMemoiAnother(i+j,arr,memo))
    memo[i]=min_jumps
    return min_jumps

# dp
def min_jumpsDp(arr):
    dp=[float("inf")]*len(arr)
    dp[0]=0
    for i in range(1,len(arr)):
        for j in range(i):
            if j+arr[j]>=i:
                dp[i]=min(dp[i],dp[j]+1)
    return dp[-1]

# O(n) time and O(1) space
def min_jumpsGreedy(arr):
    n=len(arr)
    if n==0 or arr[0]==0:
        return -1
    
    if n==1:
        return 0
    
    jumps=0
    curEnd=0
    curFarthest=0
    for i in range(n-1):
        curFarthest=max(curFarthest,i+arr[i])
        if i==curEnd:
            jumps+=1
            curEnd=curFarthest

            if curEnd>=n-1:
                return jumps
            
    return -1

print(min_jumpsRecur(0,arr))
print(min_jumpsMemoi(arr))
print(min_jumpsMemoiAnother(0,arr))
print(min_jumpsDp(arr))
print(min_jumpsGreedy(arr))