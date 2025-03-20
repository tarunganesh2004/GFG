# Stock buy and sell max 2transactions allowed

prices=[10,22,5,75,65,80]

def maxProfit(prices):
    n=len(prices)
    if n==0:
        return 0
    dp=[[0]*n for _ in range(3)]
    for i in range(1,3):
        maxDiff=-prices[0]
        for j in range(1,n):
            dp[i][j]=max(dp[i][j-1],prices[j]+maxDiff)
            maxDiff=max(maxDiff,dp[i-1][j]-prices[j])
    return dp[2][n-1]

print(maxProfit(prices)) # 87