# Rat in a Maze 

maze=[[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]

def ratInMaze(maze):
    n=len(maze)
    m=len(maze[0])
    res=[]
    visited=[[0 for _ in range(m)] for _ in range(n)]

    def isSafe(x,y):
        if x>=0 and x<n and y>=0 and y<m and maze[x][y]==1 and visited[x][y]==0:
            return True
        return False
    
    def backtrack(x,y,path):
        if x==n-1 and y==m-1:
            res.append("".join(path))
            return
        
        # mark as visited
        visited[x][y]=1
        # possible moves: D,L,R,U
        directions=[(1,0,'D'),(0,-1,'L'),(0,1,'R'),(-1,0,'U')]
        for dx,dy,move in directions:
            newX=x+dx
            newY=y+dy
            if isSafe(newX,newY):
                path.append(move)
                backtrack(newX,newY,path)
                path.pop()
        # unmark
        visited[x][y]=0
    backtrack(0,0,[])
    return res

print(ratInMaze(maze))