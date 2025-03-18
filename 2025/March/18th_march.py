# Partition Equal Subset Sum

arr=[1,5,11,5]

# recursion
def bruteForce(arr):
    def recur(cur_idx,cur_sum):
        if cur_sum==0:
            return True
        if cur_idx>=len(arr):
            return False
        # include next element
        if cur_sum-arr[cur_idx]>=0:
            if recur(cur_idx+1,cur_sum-arr[cur_idx]):
                return True
        # exclude next element
        if recur(cur_idx+1,cur_sum):
            return True
        return False
    
    total_sum=sum(arr)
    if total_sum%2!=0:
        return False
    
    return recur(0,total_sum//2)

# using lru_cache
def bruteForceMemoi(arr):
    from functools import lru_cache
    arr = tuple(arr)

    @lru_cache(None)
    def helper(cur_idx,cur_sum):
        if cur_sum==0:
            return True
        if cur_idx>=len(arr):
            return False
        # include next element
        if cur_sum-arr[cur_idx]>=0:
            if helper(cur_idx+1,cur_sum-arr[cur_idx]):
                return True
        # exclude next element
        if helper(cur_idx+1,cur_sum):
            return True
        return False
    
    total_sum=sum(arr)
    if total_sum%2!=0:
        return False
    
    return helper(0,total_sum//2)


# memoization
def subsetSumMemoi(arr):
    def recur(cur_idx,cur_sum,memo):
        if cur_sum==0:
            return True
        if cur_idx>=len(arr):
            return False
        if (cur_idx,cur_sum) in memo:
            return memo[(cur_idx,cur_sum)]
        # include next element
        if cur_sum-arr[cur_idx]>=0:
            if recur(cur_idx+1,cur_sum-arr[cur_idx],memo):
                memo[(cur_idx,cur_sum)]=True
                return True
        # exclude next element
        if recur(cur_idx+1,cur_sum,memo):
            memo[(cur_idx,cur_sum)]=True
            return True
        memo[(cur_idx,cur_sum)]=False
        return False
    
    total_sum=sum(arr)
    if total_sum%2!=0:
        return False
    
    return recur(0,total_sum//2,{})

# dp
def subsetSumDP(arr):
    total_sum=sum(arr)
    if total_sum%2!=0:
        return False
    n=len(arr)
    target=total_sum//2
    dp=[[False]*(target+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,target+1):
            if j-arr[i-1]>=0:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][target]

print(subsetSumDP(arr))

print(bruteForce(arr))
print(bruteForceMemoi(arr))
print(subsetSumMemoi(arr))