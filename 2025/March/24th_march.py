# Matrix Chain Multiplication

arr=[2,1,3,4]

# brute force
def brute_force(arr):
    def recur(start,end):
        if start==end:
            return 0
        
        min_cost=float("inf")
        for k in range(start,end):
            left=recur(start,k)
            right=recur(k+1,end)
            cost=left+right+(arr[start-1]*arr[k]*arr[end])
            min_cost=min(min_cost,cost)
        
        return min_cost
    
    return recur(1,len(arr)-1)

# using lru_cache
def memoi_brute_force(arr):
    from functools import lru_cache
    @lru_cache(None)
    def recur(start,end):
        if start==end:
            return 0
        
        min_cost=float("inf")
        for k in range(start,end):
            left=recur(start,k)
            right=recur(k+1,end)
            cost=left+right+(arr[start-1]*arr[k]*arr[end])
            min_cost=min(min_cost,cost)
        
        return min_cost
    
    return recur(1,len(arr)-1)

# memoization
def memoization(arr):
    def recurMemo(start,end,memo):
        if start==end:
            return 0
        
        if (start,end) in memo:
            return memo[(start,end)]
        
        min_cost=float("inf")
        for k in range(start,end):
            left=recurMemo(start,k,memo)
            right=recurMemo(k+1,end,memo)
            cost=left+right+(arr[start-1]*arr[k]*arr[end])
            min_cost=min(min_cost,cost)
        
        memo[(start,end)]=min_cost
        return memo[(start,end)]
    
    return recurMemo(1,len(arr)-1,{})

# dp
def dp(arr):
    n=len(arr)
    dp=[[0]*n for _ in range(n)]
    for l in range(2,n):  # noqa: E741
        for i in range(1,n-l+1):
            j=i+l-1
            dp[i][j]=float("inf") # type: ignore
            for k in range(i,j):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+(arr[i-1]*arr[k]*arr[j]))
    
    return dp[1][n-1]

print(brute_force(arr)) # 20
print(memoi_brute_force(arr)) # 20
print(memoization(arr)) # 20
print(dp(arr)) # 20