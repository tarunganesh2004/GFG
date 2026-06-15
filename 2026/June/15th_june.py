# Minimum cost to fill given weight in a bag 

cost=[20,10,4,50,100]
w=5

def bruteForce(cost,w):
    from functools import lru_cache
    @lru_cache(None)
    def solve(i,w,cost):
        if w==0:
            return 0
        if i==len(cost):
            return float('inf')
        
        skip=solve(i+1,w,cost)
        take=float('inf')
        weight=i+1
        if cost[i]!=-1 and weight<=w:
            take=cost[i]+solve(i,w-weight,cost)
        return min(skip,take)
    
    ans=solve(0,w,cost)
    return -1 if ans==float('inf') else ans

# memoization (top-down dp)
def minimumCost(cost,w):
    n=len(cost)
    dp=[[-1]*(w+1) for _ in range(n+1)]
    def solve(i,rem):
        if rem==0:
            return 0
        
        if i==n:
            return float('inf')
        
        if dp[i][rem]!=-1:
            return dp[i][rem]
        
        skip=solve(i+1,rem)
        take=float('inf')

        weight=i+1
        if cost[i]!=-1 and weight<=rem:
            take=cost[i]+solve(i,rem-weight)
        
        dp[i][rem]=min(skip,take)

        return dp[i][rem]
    
    ans=solve(0,w)
    return -1 if ans==float('inf') else ans


print(bruteForce(cost,w))