# Coverage of all Zeroes in a Binary Matrix

mat=[[1,1,1,0],[1,0,0,1]]

def findCoverage(mat):
    m=len(mat)
    n=len(mat[0])

    total=0

    for i in range(m):
        for j in range(n):

            if mat[i][j]==0:
                # left
                for k in range(j-1,-1,-1):
                    if mat[i][k]==1:
                        total+=1
                        break 
                
                # right
                for k in range(j+1,n):
                    if mat[i][k]==1:
                        total+=1
                        break 
                
                # up
                for k in range(i-1,-1,-1):
                    if mat[k][j]==1:
                        total+=1
                        break 
                
                # down 
                for k in range(i+1,m):
                    if mat[k][j]==1:
                        total+=1
                        break 

    return total 

print(findCoverage(mat))