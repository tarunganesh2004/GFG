# Ways to reach the nth Stair

n=1

# recursion
def recursion(n):
    def f(n):
        if n==0:
            return 1
        if n<0:
            return 0
        return f(n-1)+f(n-2)+f(n-3)
    return f(n)

# memoization
def memoi(n):
    def f(n,memo):
        if n==0:
            return 1
        if n<0:
            return 0
        if memo[n]!=-1:
            return memo[n]
        
        memo[n]=f(n-1,memo)+f(n-2,memo)+f(n-3,memo)
        return memo[n]
    memo=[-1 for i in range(n+1)]
    return f(n,memo)

# dp
def countWays(n):
    dp=[0 for i in range(n+1)]
    dp[0]=1
    for i in range(1,n+1):
        dp[i]+=dp[i-1]
        if i>=2:
            dp[i]+=dp[i-2]
        if i>=3:
            dp[i]+=dp[i-3]
    return dp[n] 

print(recursion(n)) # 1
print(memoi(n)) # 1