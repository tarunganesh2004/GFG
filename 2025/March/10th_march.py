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

print(brute_force(s1,s2)) # 1
print(memoiz(s1,s2)) # 1