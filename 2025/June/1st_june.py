# Count Pairs Sum in Matrices

n=3
x=21
mat1 = [[1, 5, 6], [8, 10, 11], [15, 16, 18]]
mat2 = [[2, 4, 7], [9, 10, 12], [13, 16, 20]]

def countPairs(mat1,mat2,x):
    n=len(mat1)*len(mat1[0])
    i,j=0,n-1
    count = 0
    while i<n and j>=0:
        r1,c1=divmod(i, len(mat1[0]))
        r2,c2=divmod(j, len(mat1[0]))

        s=mat1[r1][c1] + mat2[r2][c2]
        if s<x:
            i+=1
        elif s>x:
            j-=1
        else:
            count += 1
            i += 1
            j -= 1
    return count

print(countPairs(mat1, mat2, x))  