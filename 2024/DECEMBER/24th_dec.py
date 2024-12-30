# Search in a Sorted Matrix

mat=[[1,5,9],[14,20,21],[30,34,43]]
x=14

def search(mat,x):
    n=len(mat)
    m=len(mat[0])
    i=0
    j=m-1
    while i<n and j>=0:
        if mat[i][j]==x:
            return [i,j]
        elif mat[i][j]>x:
            j-=1
        else:
            i+=1
    return [-1,-1]

def search_another_way(mat,x):
    rows,cols=len(mat),len(mat[0])
    l,h=0,rows*cols-1  # noqa: E741
    while l<=h:
        mid=(l+h)//2
        i,j=mid//cols,mid%cols

        if mat[i][j]==x:
            return [i,j] # return True
        elif mat[i][j]<x:
            l=mid+1  # noqa: E741
        else:
            h=mid-1
    return [-1,-1] # return False

print(search(mat,x))