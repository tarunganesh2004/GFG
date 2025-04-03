# Rotten Oranges

mat=[[0,1,2],[0,1,2],[2,1,1]]

def orangesRotting(mat):
    dir=[(0,1),(0,-1),(1,0),(-1,0)]
    q=[]
    n=len(mat)
    m=len(mat[0])
    fresh=0
    for i in range(n):
        for j in range(m):
            if mat[i][j]==1:
                fresh+=1
            elif mat[i][j]==2:
                q.append((i,j))

    min_time=0
    while q and fresh>0:
        size=len(q)
        for _ in range(size):
            x,y=q.pop(0)
            for dx,dy in dir:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and mat[nx][ny]==1:
                    mat[nx][ny]=2
                    fresh-=1
                    q.append((nx,ny))
        min_time+=1
    if fresh==0:
        return min_time
    else:
        return -1

print(orangesRotting(mat))