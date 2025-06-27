# Mobile Numeric Keypad

n=1

def getCount(n):
    def solve(dp,m,n,idx):
        if n==1:
            return 1
        if dp[n][idx]!=-1:
            return dp[n][idx]
        
        res=0
        for i in m[idx]:
            res+=solve(dp,m,n-1,i)
        dp[n][idx]=res
        return res
    
    m = [
        [0, 8],
        [1, 2, 4],
        [1, 2, 3, 5],
        [2, 3, 6],
        [1, 4, 5, 7],
        [2, 4, 5, 6, 8],
        [3, 5, 6, 9],
        [4, 7, 8],
        [5, 7, 8, 9, 0],
        [6, 8, 9],
    ]
    dp=[[-1]*10 for _ in range(n+1)]

    res=0
    for i in range(len(m)):
        res+=solve(dp,m,n,i)
    return res

print(getCount(n))  # Output: 10