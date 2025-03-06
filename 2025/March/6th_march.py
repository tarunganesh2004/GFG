# Longest Common Subsequence

s1="ABCDGH"
s2="AEDFHR"

# brute force recursive
def lcs_recursive(s1,s2):
    if not s1 or not s2:
        return 0
    if s1[0]==s2[0]:
        return 1+lcs_recursive(s1[1:],s2[1:])
    return max(lcs_recursive(s1[1:],s2),lcs_recursive(s1,s2[1:]))

# memoization
def lcs_memoization(s1,s2):
    cache={}
    def helper(i,j):
        if i>=len(s1) or j>=len(s2):
            return 0
        if (i,j) in cache:
            return cache[(i,j)]
        if s1[i]==s2[j]:
            cache[(i,j)]=1+helper(i+1,j+1)
        else:
            cache[(i,j)]=max(helper(i+1,j),helper(i,j+1))
        return cache[(i,j)]
    return helper(0,0)

# tabulation
def lcs_dp(s1,s2):
    m,n=len(s1),len(s2)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]



print(lcs_recursive(s1,s2)) # 3
print(lcs_memoization(s1,s2)) # 3
print(lcs_dp(s1,s2)) # 3