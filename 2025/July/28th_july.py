# Make Matrix Beautiful

mat=[[1,2],[3,4]]

def balanceSums(mat):
    n=len(mat)
    res=0
    maxSum=0

    # find maximum sum across all rows
    for i in range(n):
        sum=0
        for j in range(n):
            sum+=mat[i][j]
        maxSum=max(maxSum,sum)
    # find maximum sum across all columns
    for j in range(n):
        sum=0
        for i in range(n):
            sum+=mat[i][j]
        maxSum=max(maxSum,sum)

    # sum of operations across all rows
    for i in range(n):
        sum=0
        for j in range(n):
            sum+=mat[i][j]
        res+=maxSum-sum
    
    return res

print(balanceSums(mat))