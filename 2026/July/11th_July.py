# Longest Possible Route in a Matrix with Hurdles

mat = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

xs=0
ys=0
xd=1
yd=7

# backtracking 
def longestPath(mat,xs,ys,xd,yd):
    n=len(mat)
    m=len(mat[0])
    if mat[xs][ys]==0 or mat[xd][yd]==0:
        return -1 
    vis=[[False]*m for _ in range(n)]

    def dfs(r,c):
        if r<0 or r>=n or c<0 or c>=m:
            return float('-inf')
        
        if mat[r][c]==0:
            return float('-inf')
        # if already visited
        if vis[r][c]:
            return float('-inf')
        
        if r==xd and c==yd:
            return 0
        
        vis[r][c]=True 

        best=max(
            dfs(r-1,c),
            dfs(r+1,c),
            dfs(r,c-1),
            dfs(r,c+1)
        )

        # backtrack
        vis[r][c]=False 

        if best==float('-inf'):
            return float('-inf')
        return best+1
    
    ans=dfs(xs,ys)
    return -1 if ans==float('-inf') else ans

print(longestPath(mat,xs,ys,xd,yd))