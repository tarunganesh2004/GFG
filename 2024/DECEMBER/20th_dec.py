# Spirally traversing a matrix

mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

def spiralTraverse(mat):
    res=[]
    while mat:
        res+=mat.pop(0)
        if mat and mat[0]:
            for row in mat:
                res.append(row.pop())
        if mat:
            res+=mat.pop()[::-1]
        if mat and mat[0]:
            for row in mat[::-1]:
                res.append(row.pop(0))
    return res

print(spiralTraverse(mat))