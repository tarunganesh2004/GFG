# Unique Paths in a Grid

n=3
m=3
grid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]

def uniquePaths(grid):
    n = len(grid)
    m = len(grid[0])
    
    if grid[0][0] == 1 or grid[n-1][m-1] == 1:
        return 0
    
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
    
    return dp[n-1][m-1]

print(uniquePaths(grid))  # Output: 2