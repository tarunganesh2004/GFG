# Find the Number of Islands

grid = [
    ["L", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "L"],
    ["L", "W", "W", "L", "L"],
    ["W", "W", "W", "W", "W"],
    ["L", "W", "L", "L", "W"],
]

def numIslands(grid):
    # using bfs
    dir=[[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]] # 8 directions
    def bfs(r,c,vis,grid):
        vis[r][c]=1
        q=[(r,c)]
        while q:
            row,col=q.pop(0)
            for d in dir:
                newRow=row+d[0]
                newCol=col+d[1]
                if 0<=newRow<len(grid) and 0<=newCol<len(grid[0]) and not vis[newRow][newCol] and grid[newRow][newCol]=="L":
                    vis[newRow][newCol]=1
                    q.append((newRow,newCol))
    
    n=len(grid)
    m=len(grid[0])
    vis=[[0 for _ in range(m)] for _ in range(n)]
    count=0
    for i in range(n):
        for j in range(m):
            if vis[i][j]==0 and grid[i][j]=="L":
                bfs(i,j,vis,grid)
                count+=1
    return count

print(numIslands(grid))