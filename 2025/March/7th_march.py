# Longest Palindromic Subsequence

s="bbabcbcab"

# recursive

def lps_recursive(s,i,j): # O(2^n) 
    if i==j: # if there is only one character
        return 1
    if i>j:
        return 0
    
    if s[i]==s[j]:
        return 2+lps_recursive(s,i+1,j-1) # 2 characters are same, so 2 is added and the remaining string is checked
    else:
        return max(lps_recursive(s,i+1,j),lps_recursive(s,i,j-1))
    
# Memoization - O(n^2)
def lps_memo(s,i,j,memo):
    if i==j:
        return 1
    if i>j:
        return 0
    
    # check if the value is already calculated
    if (i,j) in memo:
        return memo[(i,j)]
    
    if s[i]==s[j]:
        memo[(i,j)]=2+lps_memo(s,i+1,j-1,memo)
    else:
        memo[(i,j)]=max(lps_memo(s,i+1,j,memo),lps_memo(s,i,j-1,memo))
    return memo[(i,j)]

# Tabulation - O(n^2) bottom up
def lps_dp(s):
    n=len(s)
    dp=[[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i]=1 # single character is always a palindrome

    # start from the end
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if s[i]==s[j]:
                dp[i][j]=2+dp[i+1][j-1]
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j-1])
    return dp[0][-1]


    
print(lps_recursive(s,0,len(s)-1)) # 7
print(lps_memo(s,0,len(s)-1,{})) # 7
print(lps_dp(s)) # 7