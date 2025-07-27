# Set Matrix Zeroes

mat=[[1,-1,1],[-1,0,1],[1,-1,1]]

def setZeroes(mat):
    m, n = len(mat), len(mat[0])
    row=[-1]*n 
    col=[-1]*m

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                row[j] = 1
                col[i] = 1
    for i in range(n):
        if row[i]==1:
            for j in range(m):
                mat[j][i] = 0

    for i in range(m):
        if col[i]==1:
            for j in range(n):
                mat[i][j] = 0
    return mat

print(setZeroes(mat))