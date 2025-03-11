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

print(recursion(n)) # 1