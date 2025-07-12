# Gold Mine Problem

mat=[[1,3,3],[2,1,4],[0,6,4]]

# recursion
def bruteForce(mat): # O(3^(rows*cols)) - exponential time complexity
    n,m=len(mat),len(mat[0])
    def dfs(x,y,mat):
        if x<0 or x>=n or y<0 or y>=m:
            return 0
        rightUpper=dfs(x-1,y+1,mat)
        right=dfs(x,y+1,mat)
        rightLower=dfs(x+1,y+1,mat)
        return mat[x][y] + max(rightUpper, right, rightLower)
    res=0
    for i in range(n):
        res=max(res, dfs(i, 0, mat))
    return res

# using lru_cache
def memoized(mat): # O(rows*cols)
    from functools import lru_cache
    n,m=len(mat),len(mat[0])
    @lru_cache(None)
    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return 0
        rightUpper = dfs(x - 1, y + 1)
        right = dfs(x, y + 1)
        rightLower = dfs(x + 1, y + 1)
        return mat[x][y] + max(rightUpper, right, rightLower)
    
    max_gold = 0
    for row in range(n):
        max_gold = max(max_gold, dfs(row, 0))
    return max_gold

# memoization top-down approach
def maxGoldMemo(mat):
    n,m=len(mat),len(mat[0])
    res=0
    memo=[[-1 for _ in range(m)] for _ in range(n)]

    def collectGold(x,y,mat,memo):
        n=len(mat)
        m=len(mat[0])
        if x<0 or x>=n or y<0 or y>=m:
            return 0
        if memo[x][y]!=-1:
            return memo[x][y]
        
        rightUpper=collectGold(x-1,y+1,mat,memo)
        right=collectGold(x,y+1,mat,memo)
        rightLower=collectGold(x+1,y+1,mat,memo)
        memo[x][y]=mat[x][y] + max(rightUpper, right, rightLower)
        return memo[x][y]
    
    for i in range(n):
        res=max(res, collectGold(i, 0, mat, memo))
    return res

# DP Bottom-Up Approach
def maxGoldDP(mat):
    n,m=len(mat),len(mat[0])
    dp=[[0 for _ in range(m)] for _ in range(n)]

    # fill the last column with initial gold values
    for i in range(n):
        dp[i][m-1] = mat[i][m-1]
    # fill the dp table from second last column to the first column
    for y in range(m-2,-1,-1):
        for x in range(n):
            rightUpper = dp[x-1][y+1] if x > 0 else 0
            right = dp[x][y+1]
            rightLower = dp[x+1][y+1] if x < n-1 else 0
            dp[x][y] = mat[x][y] + max(rightUpper, right, rightLower)
    # find the maximum gold collected from the first column
    largest = 0
    for i in range(n):
        largest = max(largest, dp[i][0])
    return largest


print(bruteForce(mat))  # Output: 12
print(memoized(mat))  # Output: 12
print(maxGoldMemo(mat))  # Output: 12
print(maxGoldDP(mat))  # Output: 12