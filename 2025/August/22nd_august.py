# Median in a row-wise sorted matrix

mat=[[1, 3, 5],
      [2, 6, 9],
      [3, 6, 9]]

# brute force
def bruteForce(mat):
    arr=[]
    for row in mat:
        for ele in row:
            arr.append(ele)
    arr.sort()
    left=0
    right=len(arr)-1
    mid=(left+right)//2
    return arr[mid]

# binary search
def optimized(mat):
    def count_smaller_equal(row,x):
        left,right=0,len(row)
        while left < right:
            mid = (left + right) // 2
            if row[mid] <= x:
                left = mid + 1
            else:
                right = mid
        return left
    
    m,n=len(mat),len(mat[0])
    low=min(row[0] for row in mat)
    high=max(row[-1] for row in mat)
    desired= (m * n + 1) // 2  # median position in a flattened array
    while low<high:
        mid= (low + high) // 2
        count=0
        for row in mat:
            count += count_smaller_equal(row, mid)
        if count < desired:
            low = mid + 1
        else:
            high = mid
    return low


print(bruteForce(mat))
print(optimized(mat))