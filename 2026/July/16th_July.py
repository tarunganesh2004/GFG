# Numbers with given digit sum 

n=2
sum=2

# bruteforce
def bruteForce(n,sum):
    c=0
    def dfs(i,cur_sum):
        nonlocal c
        if i==n:
            if cur_sum==sum:
                c+=1
            return 
        
        start=1 if i==0 else 0
        for digit in range(start,10):
            dfs(i+1,cur_sum+digit)
    dfs(0,0)
    return c

# memoization
def memoization(n,sum):
    memo=[[-1]*(sum+1) for _ in range(n+1)]
    def dfs(i,cur_sum):
        if cur_sum>sum:
            return 0
        
        if i==n:
            return 1 if cur_sum==sum else 0
        
        if memo[i][cur_sum]!=-1:
            return memo[i][cur_sum]
        
        ans=0
        start=1 if i==0 else 0

        for digit in range(start,10):
            ans+=dfs(i+1,cur_sum+digit)
        
        memo[i][cur_sum]=ans
        return ans 
    ans=dfs(0,0)
    return ans if ans>0 else -1

def tabulation(n,target):
    dp=[[0]*(target+1) for _ in range(n+1)]
    # from recursion
    # if i==n: return 1 if cur_sum==target else 0
    # so dp[n][target]=1
    dp[n][target]=1

    # dp[i] depends on dp[i+1]

    for i in range(n-1,-1,-1):
        start=1 if i==0 else 0
        for cur_sum in range(target,-1,-1):

            ans=0
            for digit in range(start,10):
                if cur_sum+digit<=target:
                    ans+=dp[i+1][cur_sum+digit]
            dp[i][cur_sum]=ans 

    return dp[0][0]

print(bruteForce(n,sum))

print(memoization(n,sum))

print(tabulation(n,sum))