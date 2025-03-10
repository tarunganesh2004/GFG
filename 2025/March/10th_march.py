# Edit Distance

s1="geek"
s2="gesek"

# brute force
def brute_force(s1,s2):
    def helper(s1,s2,m,n):
        if m==0:
            return n
        if n==0:
            return m
        if s1[m-1]==s2[n-1]:
            return helper(s1,s2,m-1,n-1)
        return 1+min(helper(s1,s2,m,n-1),helper(s1,s2,m-1,n),helper(s1,s2,m-1,n-1))
    return helper(s1,s2,len(s1),len(s2))

# memoization
def memoiz(s1,s2):
    def helper(s1,s2,m,n,dp):
        if m==0:
            return n
        if n==0:
            return m
        if dp[m][n]!=-1:
            return dp[m][n]
        if s1[m-1]==s2[n-1]:
            dp[m][n]=helper(s1,s2,m-1,n-1,dp)
            return dp[m][n]
        dp[m][n]=1+min(helper(s1,s2,m,n-1,dp),helper(s1,s2,m-1,n,dp),helper(s1,s2,m-1,n-1,dp))
        return dp[m][n]
    dp=[[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    return helper(s1,s2,len(s1),len(s2),dp)

# tabulation
def dp(s1,s2):
    m=len(s1)
    n=len(s2)
    dp=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
    return dp[m][n]


print(brute_force(s1,s2)) # 1
print(memoiz(s1,s2)) # 1
print(dp(s1,s2)) # 1