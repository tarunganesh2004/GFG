# Search in fully rotated sorted 2D Matrix

x=3
mat=[[7,8,9,10],[11,12,13,1],[2,3,4,5]]

# brute force
def bruteForce(mat,x):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == x:
                return True
    return False

# optimized
def searchMatrix(mat,x):
    n,m= len(mat), len(mat[0])
    low,high=0,n*m-1

    while low <= high:
        mid=low+(high-low)//2

        # convert 1d index to 2d coordinates
        row= mid // m
        col= mid % m
        midVal= mat[row][col]

        if midVal == x:
            return True
        
        # get value at virtual low position
        lowRow= low // m
        lowCol= low % m
        lowVal= mat[lowRow][lowCol]

        # if left side is sorted
        if lowVal <= midVal:
            # check if x is in the left side
            if lowVal <= x < midVal:
                high= mid-1
            else:
                low= mid+1
        else:
            # right side is sorted
            highRow= high // m
            highCol= high % m
            highVal= mat[highRow][highCol]
            # check if x is in the right side
            if midVal < x <= highVal:
                low= mid+1
            else:
                high= mid-1
    return False

print(bruteForce(mat, x))