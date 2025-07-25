# Maximum Circular Subarray Sum(Hard)

arr= [8, -8, 9, -9, 10, -11, 12]

# brute force

def bruteForce(arr):
    n=len(arr)
    res=arr[0]

    for i in range(n):
        curSum=0

        for j in range( n):
            idx=(i+j)%n
            curSum+=arr[idx]
            res=max(res, curSum)
    return res

# using prefix and suffix sum 
def maxCircularSum(arr):
    n=len(arr)

    suffixSum=arr[n-1]
    maxSuffix=[0]*(n+1)
    maxSuffix[n-1]=arr[n-1]

    for i in range(n-2, -1, -1):
        suffixSum+=arr[i]
        maxSuffix[i]=max(maxSuffix[i+1], suffixSum)

    circularSum=arr[0]
    normalSum=arr[0]

    curSum=0
    prefix=0

    for i in range(n):
        # kadane algorithm
        curSum=max(arr[i], curSum + arr[i])
        normalSum=max(normalSum, curSum)

        prefix+=arr[i]
        circularSum=max(circularSum, prefix + maxSuffix[i+1])
    return max(normalSum, circularSum)

print(bruteForce(arr))
print(maxCircularSum(arr))