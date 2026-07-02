# Max subarray sum by removing atmost one

arr=[1,2,3,-4,5]

"""
Recursion
f(i) = max(arr[i], arr[i] + f(i-1))
           ↓
Memoization
           ↓
Tabulation
           ↓
Space Optimization
           ↓
Kadane Algorithm
"""

"""
 now for this qsn 
 f(i,deleted) --> state 
 deleted=0 means deletion not used yet, 1 means deletion already used
 f(i,0) --> kadane
 f(i,1) -> Maximum subarray sum ending at i after using one deletion.
 f(i,1) has 2 cases 
 1) deletion happened earlier --> then simply add current element arr[i]+f(i-1,1)
 2) delete the current element: --> if we delete arr[i], then the subarray effectively ends at i-1, and till i-1 we havent used any deletion so f(i-1,0)

Case 1:
... deleted something earlier ... + arr[i]

f(i-1,1) -----------------------> f(i,1)


Case 2:
Delete arr[i]

f(i-1,0) -----------------------> f(i,1)

so 
 f(i,1)=max(
 arr[i]+f(i-1,1)
 f(i-1,0)
 )

"""

# recursion
def recursion(arr):
    # from functools import lru_cache
    n=len(arr)
    ans=float('-inf')
    # @lru_cache(None)
    def f(i,deleted):
        if i==0:
            if deleted==0: 
                return arr[0]
            # subarray must remain not empty so f(0,1) doesnt exist
            return float('-inf')

        if deleted==0:
            return max(arr[i],arr[i]+f(i-1,0))
        return max(arr[i]+f(i-1,1),f(i-1,0))

    for i in range(n):
        ans=max(ans,f(i,0),f(i,1))
    return ans 

# memoization
def memoization(arr):
    n=len(arr)
    memo={} # 2d list can be used, dp=[[None]*2 for _ in range(n)]
    def f(i,deleted):
        if i==0:
            if deleted==0:
                return arr[0]
            return float('-inf')

        if (i,deleted) in memo:
            return memo[(i,deleted)]

        if deleted == 0:
            ans = max(arr[i], arr[i] + f(i - 1, 0))
        else:
            ans = max(arr[i] + f(i - 1, 1), f(i - 1, 0))

        memo[(i,deleted)] = ans
        return ans
    
    ans=float('-inf')
    for i in range(n):
        ans=max(ans,f(i,0),f(i,1))
    return ans

# dp
def tabulation(arr):
    n=len(arr)
    dp=[[0]*2 for _ in range(n)]
    # base cases, from recursion f(0,0)=arr[0],f(0,1)=-inf 
    dp[0][0]=arr[0]

    dp[0][1]=float('-inf') # type: ignore

    ans=arr[0]
    for i in range(1,n):
        # no deletion used 
        dp[i][0]=max(arr[i],arr[i]+dp[i-1][0])

        # one deletion used
        dp[i][1]=max(arr[i]+dp[i-1][1],dp[i-1][0])

        ans=max(ans,dp[i][0],dp[i][1])
    return ans 

# space optimized
def spaceOptimized(arr):
    """
    from dp 
    dp[i][0]<- previous row, dp[i][1] <- previous row only
    so prev0=dp[i-1][0]
    prev1=dp[i-1][1] and compute curr0,curr1
    """
    noDel=arr[0]
    oneDel=float('-inf') # one del means max subarray sum ending at current index after using one deletion,
    # at index 0,if we have one element, if we delete that it becomes an empty subarray
    # but in the qsn they gave subarray should not be empty so this state is impossible
    ans=arr[0]
    for i in range(1,len(arr)):
        newNoDel=max(arr[i],arr[i]+noDel)

        newOneDel=max(arr[i]+oneDel,noDel)

        noDel=newNoDel
        oneDel=newOneDel

        ans=max(ans,noDel,oneDel)
    return ans

print(recursion(arr))

print(memoization(arr))
print(tabulation(arr))
print(spaceOptimized(arr))

"""
Pattern learnt today 

Kadane:
state = f(i)

One deletion allowed:
state = f(i, deleted)

Recurrence depends only on i-1
↓
Tabulation: 2 columns
↓
Space Optimization: 2 variables
"""
