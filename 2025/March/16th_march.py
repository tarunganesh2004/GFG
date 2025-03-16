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
def min_jumpsMemoiAnother(arr, memo={}):
    if i>=len(arr)-1:
        return 0
    if arr[i]==0:
        return float("inf")
    if i in memo:
        return memo[i]
    min_jumps=float("inf")
    for j in range(1,arr[i]+1):
        min_jumps=min(min_jumps,1+min_jumpsMemoi(i+j,arr))
    memo[i]=min_jumps
    return min_jumps

print(min_jumpsRecur(0,arr))
print(min_jumpsMemoi(arr))