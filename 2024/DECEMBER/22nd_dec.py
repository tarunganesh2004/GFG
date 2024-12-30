# Search in a row-column sorted matrix

mat=[[3, 30, 38],[44, 52, 54],[57, 60, 69]]
x=62
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x1=3

def search(mat,x):
    n=len(mat)
    left=0
    right=n-1
    while left<n and right>=0:
        if mat[left][right]==x:
            return [left,right]
        elif mat[left][right]>x:
            right-=1
        else:
            left+=1
    return [-1,-1]

print(search(mat,x))
print(search(m1,x1))