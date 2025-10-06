# The Knight's Tour Problem

n=5

def knightTour(n):
    di=((1,2),(2,1),(-1,2),(2,-1),(1,-2),(-2,1),(-1,-2),(-2,-1))
    res=[]

    def backtrack(pos,mat,step):
        if step==n**2:
            raise
        for dx,dy in di:
            nx,ny=pos[0]+dx,pos[1]+dy
            if 0<=nx<n and 0<=ny<n and mat[nx][ny]==-1:
                mat[nx][ny]=step
                backtrack((nx,ny),mat,step+1)
                mat[nx][ny]=-1
                
    mat=[[-1]*n for i in range(n)]
    mat[0][0]=0
    try:
        backtrack((0,0),mat,1)
    except Exception:
        res=mat 
    return res

print(knightTour(n))