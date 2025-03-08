# Longest Palindrome in a String

s="forgeeksskeegfor"

# brute force
def bruteForce(s):
    max_len=0
    max_string=""
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[i:j+1]==s[i:j+1][::-1]:
                if len(s[i:j+1])>max_len:
                    max_len=len(s[i:j+1])
                    max_string=s[i:j+1]
    return max_string

# recursive
def recursive(s):
    if s==s[::-1]:
        return s
    else:
        s1=recursive(s[1:])
        s2=recursive(s[:-1])
        if len(s1)>len(s2):
            return s1
        else:
            return s2

# memoization
def memoi(s,memo):
    if s in memo:
        return memo[s]
    if s==s[::-1]:
        memo[s]=s
        return s
    else:
        s1=memoi(s[1:],memo)
        s2=memoi(s[:-1],memo)
        if len(s1)>len(s2):
            memo[s]=s1
            return s1
        else:
            memo[s]=s2
            return s2
        
# dp
def dp(s):
    n=len(s)
    dp=[[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i]=1
    max_len=1
    start=0
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if s[i]==s[j]:
                if j-i==1 or dp[i+1][j-1]:
                    dp[i][j]=1
                    if j-i+1>max_len:
                        max_len=j-i+1
                        start=i
    return s[start:start+max_len]

# Expand around center
def optimized(s):
   
    def expandCenter(s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    
    max_palin=""
    for i in range(len(s)):
        odd_palin=expandCenter(s,i,i)
        even_palin=expandCenter(s,i,i+1)
        if len(odd_palin)>len(max_palin):
            max_palin=odd_palin
        if len(even_palin)>len(max_palin):
            max_palin=even_palin
    return max_palin

print(optimized(s)) # geeksskeeg


print(dp(s)) # geeksskeeg
        
print(memoi(s,{})) # geeksskeeg

print(bruteForce(s)) # geeksskeeg
print(recursive(s)) # geeksskeeg