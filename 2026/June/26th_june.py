# Count Matching Subsequences

s1="geeksforgeeks"
s2="gks"

# brute force
def countWaysBrute(s1,s2): # O(2^n)
    mod=10**9+7
    res=0
    n=len(s2)
    def solve(i,cur):
        nonlocal res 

        if i==len(s1):
            if cur==s2:
                res+=1
            return 
        
        solve(i+1,cur+s1[i])     

        # skip
        solve(i+1,cur)

    solve(0,"")
    return res%mod 

# other bruteforce
def memoizedSolution(s1,s2):  # this can be optimized using lru_cache
    # this is better than above, bcz instead of building entire string we can keep track of how much of s2 has been matched 
    from functools import lru_cache
    @lru_cache(None)

    # no.of ways to form s2[j:] using s1[i:]
    def solve(i,j):
        if j==len(s2):
            return 1 
        
        if i==len(s1):
            return 0 
        
        # skip
        ans=solve(i+1,j)

        # take current character if it matches
        if s1[i]==s2[j]:
            ans+=solve(i+1,j+1)
        
        return ans 
    
    return solve(0,0)

# dp code
def countWays(s1,s2):
    n=len(s1)
    m=len(s2)

    dp=[[0]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][m]=1 # empty target can always be formed

    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):

            # skip current character
            dp[i][j]=dp[i+1][j]

            # match current character if possible
            if s1[i]==s2[j]:
                dp[i][j]+=dp[i+1][j+1]
    
    return dp[0][0]


print(countWaysBrute(s1,s2))
print(memoizedSolution(s1,s2))
print(countWays(s1,s2))