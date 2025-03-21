# Stickler Thief

arr=[6,5,5,7,4]

# recursion
def brute_force(arr):
    def recur(cur_idx,n):
        if cur_idx>=n:
            return 0
        
        # include current
        include=arr[cur_idx]+recur(cur_idx+2,n)
        # exclude current
        exclude=recur(cur_idx+1,n)
        return max(include,exclude)
    
    return recur(0,len(arr))

# using lru_cache
def brute_force_memoi(arr):
    from functools import lru_cache
    arr=tuple(arr)

    @lru_cache(None)
    def recur(cur_idx,n):
        if cur_idx>=n:
            return 0
        
        # include current
        include=arr[cur_idx]+recur(cur_idx+2,n)
        # exclude current
        exclude=recur(cur_idx+1,n)
        return max(include,exclude)
    
    return recur(0,len(arr))

# memoization
def memoization(arr):
    memo={}
    def recurMemo(cur_idx,n,memo):
        if cur_idx>=n:
            return 0
        
        if cur_idx in memo:
            return memo[cur_idx]
        
        # include current
        include=arr[cur_idx]+recurMemo(cur_idx+2,n,memo)
        # exclude current
        exclude=recurMemo(cur_idx+1,n,memo)

        memo[cur_idx]=max(include,exclude)
        return memo[cur_idx]
    
    return recurMemo(0,len(arr),memo)

# Dp
def dp(arr):
    n=len(arr)
    dp=[0]*(n+2)
    dp[n]=0
    dp[n+1]=0

    for i in range(n-1,-1,-1):
        dp[i]=max(arr[i]+dp[i+2],dp[i+1])
    
    return dp[0]


print(brute_force(arr)) # 15
print(brute_force_memoi(arr)) # 15
print(memoization(arr)) # 15
print(dp(arr)) # 15