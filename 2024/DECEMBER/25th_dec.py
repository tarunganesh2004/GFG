# Set Matrix Zeroes
# You are given a 2D matrix mat[][] of size n×m. The task is to modify the matrix such that if mat[i][j] is 0, all the elements in the i-th row and j-th column are set to 0 and do it in constant space complexity.


mat = [[1, -1, 1], [-1, 0, 1], [1, -1, 1]]
def setMatrixZeroesBruteForce(mat):
    n=len(mat)
    m=len(mat[0])

    # Create a copy of the original matrix
    copy=[[0 for _ in range(m)] for _ in range(n)]

    # Copy the original matrix to the copy matrix
    for i in range(n):
        for j in range(m):
            copy[i][j]=mat[i][j]
    
    # Traverse the original matrix
    for i in range(n):
        for j in range(m):
            if mat[i][j]==0:
                for k in range(n):
                    copy[k][j]=0
                for k in range(m):
                    copy[i][k]=0
    return copy

# def setZeroesBetterWay(mat):


print(setMatrixZeroesBruteForce(mat))