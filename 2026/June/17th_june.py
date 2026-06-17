# Cut rope to maximize product

n=5
# brute force
def bruteForce(n):
    from functools import lru_cache
    @lru_cache(None)
    def solve(n):
        ans=0
        for i in range(1,n):
            ans=max(ans,i*max(n-i,solve(n-i)))
        return ans 
    
    return solve(n)

# memoization
def maxProduct(n):
    dp=[-1]*(n+1)
    def solve(length):
        if length==1:
            return 1 
        if dp[length]!=-1:
            return dp[length]
        
        ans=0
        for i in range(1,length):
            ans=max(ans,i*max(length-i,solve(length-i)))
        dp[length]=ans 

        return ans
    return solve(n)

# tabulation
def bottomupDP(n):
    dp=[0]*(n+1)
    dp[1]=1
    
    for length in range(2,n+1):
        for cut in range(1,length):
            dp[length]=max(dp[length],cut*max(length-cut,dp[length-cut]))
    return dp[n]

print(bruteForce(n))
print(maxProduct(n))
print(bottomupDP(n))