# search in a row-wise sorted matrix

mat=[[3,4,9],[2,5,6],[9,25,27]]
x=9

def search(arr,x):
    lo,hi=0,len(arr)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]==x:
            return True
        elif arr[mid]<x:
            lo=mid+1
        else:
            hi=mid-1
    return False


def search_row_wise(mat,x):
    n=len(mat)
    m=len(mat[0])  # noqa: F841
    for i in range(n):
        if search(mat[i],x):
            return True # return [i,search(mat[i],x)]
    return False # return [-1,-1]


print(search_row_wise(mat,x))