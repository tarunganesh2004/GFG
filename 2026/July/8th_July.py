# Towers Reaching Both Stations

mat=[
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]

# brute force
def countCoordinatesBrute(mat):
    n=len(mat)
    m=len(mat[0])

    ans=0
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(n):
        for j in range(m):
            # check whether (i,j) reaches both P & Q
            # maintain a visited array before every dfs
            visited=[[False]*m for _ in range(n)]
            reachedP=[False]
            reachedQ=[False]

            def dfs(r,c):
                visited[r][c]=0

                if r==0 or c==0:
                    reachedP[0]=True 

                if r==n-1 or c==m-1:
                    reachedQ[0]=True 

                for dr,dc in dirs:
                    nr=r+dr
                    nc=c+dc 
                    if 0<=nr<n and 0<=nc<m:
                        if visited[nr][nc]:
                            continue

                        # neighbour<=current
                        if mat[nr][nc]<=mat[r][c]:
                            dfs(nr,nc)
            dfs(i,j)

            if reachedP[0] and reachedQ[0]:
                ans+=1

    return ans  # this is worst case bruteforce O(n^2*m^2)

# Brute Force:
# For every cell, perform DFS and check whether it can reach P and Q.

# Optimization:
# Instead of starting DFS from every cell,
# start DFS from all P boundary cells.

# During this DFS, traverse in the REVERSE direction
# (move to neighbours with value >= current).

# Every visited cell means:
# "This cell can reach P in the original problem."

# Similarly, start DFS from all Q boundary cells
# and mark every cell that can reach Q.

# Finally,
# answer = cells that are reachable from both DFS traversals
# (intersection of P-reachable and Q-reachable cells).

def countCoordinates(mat):
    n=len(mat)
    m=len(mat[0])

    pacific=[[False]*m for _ in range(n)]
    atlantic=[[False]*m for _ in range(n)]
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    ans=0

    def dfs(r,c,visited):
        visited[r][c]=True 
        for dr,dc in dirs:
            nr=r+dr
            nc=c+dc 
            if 0<=nr<n and 0<=nc<m:
                if visited[nr][nc]:
                    continue
                if mat[nr][nc]>=mat[r][c]:
                    dfs(nr,nc,visited)

    # pacific(P)
    for j in range(m):
        if not pacific[0][j]:
            dfs(0,j,pacific)

    for i in range(n):
        if not pacific[i][0]:
            dfs(i,0,pacific)

    # atlantic
    for j in range(m):
        if not atlantic[n - 1][j]:
            dfs(n - 1, j, atlantic)

    for i in range(n):
        if not atlantic[i][m - 1]:
            dfs(i, m - 1, atlantic)

    ans=0
    for i in range(n):
        for j in range(m):
            if pacific[i][j] and atlantic[i][j]:
                ans+=1
    return ans 


# print(countCoordinatesBrute(mat))    
print(countCoordinates(mat))