# Cut Matrix (Hard qsn)

mat=[[1,0,0],[1,1,1],[0,0,0]]
k=3

"""
we need to make exactly k-1cuts
if cut horizontal, we keep the bottom part
if vertical cut, we keep the right part

so bottom,right never changes

(top,left) --> bottom-right
so state is
solve(top,left,cuts)
bcz, bottom =rows-1, cols=cols-1 are always fixed

solve(top, left, cuts)
          │
          │
          ├── Try horizontal cut at every row
          │       │
          │       ├── top part has 1?
          │       │       │
          │       │       └── solve(r+1, left, cuts-1)
          │       │
          │
          └── Try vertical cut at every column
                  │
                  ├── left part has 1?
                  │       │
                  │       └── solve(top, c+1, cuts-1)
"""

# bruteforce
def recursion(mat,k):
    rows=len(mat)
    cols=len(mat[0])
    # check whether a rectangle has atleast one 1
    def has_one(r1,c1,r2,c2):
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                if mat[i][j]==1:
                    return True
        return False
    
    # cur rectangle starts at (top,left), ends at (rows-1,cols-1) --> this is fixed
    # only (top,left) changes
    def solve(top,left,cuts):
        if cuts==0:
            if has_one(top,left,rows-1,cols-1):
                return 1 
            return 0
        
        ans=0

        # try every horizontal cut
        for r in range(top,rows-1):
            if has_one(top,left,r,cols-1):
                # continue with the bottom part 
                ans+=solve(r+1,left,cuts-1)
        
        # try every vertical cut
        for c in range(left,cols-1):
            if has_one(top,left,rows-1,c):
                ans+=solve(top,c+1,cuts-1)

        return ans 
    
    return solve(0,0,k-1)

# # memoization
# def memoization(mat,k):
#     mod=10**9+7
#     rows=len(mat)
#     cols=len(mat[0])
#     memo={}

#     def has_one(r1,c1,r2,c2):
#         for i in range(r1,r2+1):
#             for j in range(c1,c2+1):
#                 if mat[i][j]==1:
#                     return True
#         return False

#     def solve(top,left,cuts):
#         if cuts==0:
#             return 1 if has_one(top,left,rows-1,cols-1) else 0

#         state=(top,left,cuts)
#         if state in memo:
#             return memo[state]

#         ans=0

#         #horizontal cuts
#         for r in range(top,rows-1):
#             if has_one(top,left,r,cols-1):
#                 ans+=solve(r+1,left,cuts-1)

#         # vertical cuts
#         for c in range(left,cols-1):
#             if has_one(top,left,rows-1,c):
#                 ans+=solve(top,c+1,cuts-1)

#         memo[state]=ans%mod
#         return memo[state]
#     return solve(0,0,k-1)

"""
here has_one takes extra complexity
so we need to optimize the rectangle query
--> 2D Prefix sum
we precompute number of 1s in every rectange and then rectangle contains a 1 becomes rectangle_sum>0 in O(1)

p[i][j]=number of 1s in the rectangle from (0,0) to (i-1,j-1)
we use an extra row and column 
prefix[i][j]=(mat[i-1][j-1]+prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]) 
the subtraction removes the top-left region that was counted twice
"""
# memoization
def memoization(mat,k):
    mod=10**9+7
    rows=len(mat)
    cols=len(mat[0])
    # 2d prefix sum
    prefix=[[0]*(cols+1) for _ in range(rows+1)]
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            prefix[i][j]=(
                mat[i-1][j-1]
                +prefix[i-1][j]
                +prefix[i][j-1]
                -prefix[i-1][j-1] 
            )
    # O(1) rectangle sum
    def rectangle_sum(r1,c1,r2,c2):
        return (
            prefix[r2+1][c2+1]
            -prefix[r1][c2+1]
            -prefix[r2+1][c1]
            +prefix[r1][c1]
        )

    # memoization
    memo={}
    def solve(top,left,cuts):
        if cuts==0:
            return 1 if rectangle_sum(top,left,rows-1,cols-1) else 0

        state=(top,left,cuts)
        if state in memo:
            return memo[state]

        ans=0
        # horizontal cuts
        for r in range(top,rows-1):
            if rectangle_sum(top,left,r,cols-1)>0:
                ans+=solve(r+1,left,cuts-1)

        # vertical cuts
        for c in range(left,cols-1):
            if rectangle_sum(top,left,rows-1,c)>0:
                ans+=solve(top,c+1,cuts-1)

        memo[state]=ans%mod

        return memo[state]
    return solve(0,0,k-1)


def number_of_ways(matrix, k):
    MOD = 10**9 + 7
    rows = len(matrix)
    cols = len(matrix[0])
    # 1. Build 2D prefix sum
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix[i][j] = (
                matrix[i - 1][j - 1]
                + prefix[i - 1][j]
                + prefix[i][j - 1]
                - prefix[i - 1][j - 1]
            )

    # Rectangle sum in O(1)
    def rectangle_sum(r1, c1, r2, c2):
        return (
            prefix[r2 + 1][c2 + 1]
            - prefix[r1][c2 + 1]
            - prefix[r2 + 1][c1]
            + prefix[r1][c1]
        )
    # dp[top][left][cuts]
    dp = [[[0] * k for _ in range(cols)] for _ in range(rows)]

    # Base case: cuts = 0
    for top in range(rows):

        for left in range(cols):

            if rectangle_sum(top, left, rows - 1, cols - 1) > 0:

                dp[top][left][0] = 1

    # Build cuts = 1 to k - 1
    for cuts in range(1, k):
        for top in range(rows):
            for left in range(cols):
                ans = 0
                # Horizontal cuts
                for r in range(top, rows - 1):
                    # Given-away top part has a 1
                    if rectangle_sum(top, left, r, cols - 1) > 0:

                        ans += dp[r + 1][left][cuts - 1]

                # Vertical cuts
                for c in range(left, cols - 1):
                    # Given-away left part has a 1
                    if rectangle_sum(top, left, rows - 1, c) > 0:

                        ans += dp[top][c + 1][cuts - 1]

                dp[top][left][cuts] = ans % MOD

    return dp[0][0][k - 1]


print(recursion(mat,k))

print(number_of_ways(mat,k))