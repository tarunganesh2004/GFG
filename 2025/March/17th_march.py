

arr=[3,34,4,12,5,2]
sum=9

# recursion
def bruteForce(arr,sum):
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
    return recur(0,sum)

# using lru_cache
def bruteForceMemoi(arr,sum):
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
    
    return helper(0,sum)

# memoization
def subsetSumMemoi(arr,sum):
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
            memo[(cur_idx,cur_sum)]=True # if we reach here, it means we have found a subset
            return True
        memo[(cur_idx,cur_sum)]=False
        return False
    
    return recur(0,sum,{})

# another way of memoization
def anotherWay(arr,sum):
    n=len(arr)
    memo=[[-1 for _ in range(sum+1)] for _ in range(n+1)]

    def recurMemoi(cur_idx,cur_sum,memo):
        if cur_sum==0:
            return True
        if cur_idx>=len(arr):
            return False
        if memo[cur_idx][cur_sum]!=-1:
            return memo[cur_idx][cur_sum]
        # include next element
        if cur_sum-arr[cur_idx]>=0:
            if recurMemoi(cur_idx+1,cur_sum-arr[cur_idx],memo):
                memo[cur_idx][cur_sum]=True
                return True
        # exclude next element
        if recurMemoi(cur_idx+1,cur_sum,memo):
            memo[cur_idx][cur_sum]=True
            return True
        
        memo[cur_idx][cur_sum]=False
        return False
    
    return recurMemoi(0,sum,memo)

# dp , O(n*sum) time and O(n*sum) space
def subsetSumDp(arr,sum):
    n=len(arr)
    dp=[[False for _ in range(sum+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if j<arr[i-1]:
                # exclude
                dp[i][j]=dp[i-1][j]

            else:
                # exclude or include
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
    return dp[n][sum]

print(bruteForce(arr,sum)) # True
print(bruteForceMemoi(arr,sum)) # True

print(subsetSumMemoi(arr,sum)) # True
print(anotherWay(arr,sum)) # True
print(subsetSumDp(arr,sum)) # True