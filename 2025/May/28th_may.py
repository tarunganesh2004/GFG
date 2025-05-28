# Find rectangle with corners as 1

mat = [[1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 0, 1]]

def find_rectangle_with_corners(mat):
    m,n= len(mat), len(mat[0])
    for i in range(m):
        row=mat[i]
        for j in range(i+1,m):
            count=0
            r2= mat[j]
            for k in range(n):
                if row[k]==1 and r2[k]==1:
                    count+=1
            if count>=2:
                return True
    return False

print(find_rectangle_with_corners(mat))