# Minimum Insert and Delete to Convert

a=[1,2,5,3,1]
b=[1,3,5]

# one approach is to find lcs=l, m,n=len(a),len(b)
# deletions=m-l,insertions=n-l --> O(m*n)
def bruteForce(a,b):
    m,n=len(a),len(b)
    def lcs(a,b):
        m, n = len(a), len(b)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if a[i]==b[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]
    
    l=lcs(a,b)
    insertions=n-l 
    deletions=m-l
    return deletions+insertions # this leads to tle, since its hard level,

print(bruteForce(a,b))