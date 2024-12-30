# Rotate by 90
# mat[][] = [[1, 2, 3],
#             [4, 5, 6]
#             [7, 8, 9]]
# Output: Rotated Matrix:
# [3, 6, 9]
# [2, 5, 8]
# [1, 4, 7]

mat = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
def rotateBy90(mat):
    n=len(mat)
    for k in mat:
        k.reverse() # reverse the rows

    for i in range(n):
        for j in range(i,n):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j] # now transpose
    
    return mat

print(rotateBy90(mat))