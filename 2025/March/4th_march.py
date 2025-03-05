# Longest Increasing Subsequence

arr=[5,8,3,7,9,1]

# using dp
def bruteForce(arr):
    n=len(arr)
    dp=[1]*n
    for i in range(1,n):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)

