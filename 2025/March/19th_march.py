# Stock Buy and Sell - Max K transactions Allowed

prices=[10,22,5,80]
k=2

def maxProfit(prices,k):
    n=len(prices)
    if n==0:
        return 0
    if k>=n//2:
        return sum(max(prices[i+1]-prices[i],0) for i in range(n-1))
    
    dp=[[0]*n for _ in range(k+1)]
    for i in range(1,k+1):
        maxDiff=-prices[0]
        for j in range(1,n):
            dp[i][j]=max(dp[i][j-1],prices[j]+maxDiff)
            maxDiff=max(maxDiff,dp[i-1][j]-prices[j])
    return dp[k][n-1]

print(maxProfit(prices,k)) # 87