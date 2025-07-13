# Maximum Sum of Elements not part of LIS 

arr=[4,6,1,2,3,8]

def maxSumNotInLIS(arr):
    n=len(arr)
    dp=[1]*n
    for i in range(1,n):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[i],dp[j]+1)
    max_lis_length = max(dp)
    cur_len=max_lis_length
    lis=[]
    for i in range(n-1,-1,-1):
        if dp[i]==cur_len:
            lis.append(arr[i])
            cur_len-=1
    lis=lis[::-1]
    return sum(arr) - sum(lis)

print(maxSumNotInLIS(arr))  # Output: 10