# Dice Throw

m=6
n=3
x=12

def countWays(m, n, x):
    dp = [[0 for i in range(x + 1)] for j in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, x + 1):
            for k in range(1, m + 1):
                if j - k >= 0:
                    dp[i][j] += dp[i - 1][j - k]

    return dp[n][x]

print(countWays(m, n, x))