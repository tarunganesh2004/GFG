# Exit point in a Matrix

mat=[[0,1,0],[0,1,1],[0,0,0]]

def exitPoint(mat):
    n=len(mat)
    m=len(mat[0])

    dirs=[(0,1),(1,0),(0,-1),(-1,0)]

    r,c=0,0
    cur=0
    prev=[0,0]

    while 0<=r<n and 0<=c<m:
        prev=[r,c]
        if mat[r][c]==1:
            mat[r][c]=0
            cur=(cur+1)%4
        r+=dirs[cur][0]
        c+=dirs[cur][1]
    
    return prev

print(exitPoint(mat))