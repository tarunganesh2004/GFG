# Minimum Deletions to Make a String Palindrome

s="aebcbda"

def minDeletions(s):
    r=s[::-1]
    n=len(s)
    prev=[0]*(n+1)
    for i in range(1,n+1):
        cur=[0]*(n+1)
        for j in range(1,n+1):
            if s[i-1]==r[j-1]:
                cur[j]=prev[j-1]+1
            else:
                cur[j]=max(prev[j],cur[j-1])
        prev=cur
    lcs=prev[n]
    return n-lcs
    

print(minDeletions(s))