# Max Score from Subarray Minimums

arr=[4,3,5,1]


def maxSum(arr):
    res=arr[0]+arr[1]
    for i in range(1,len(arr)-1):
        res=max(res,arr[i]+arr[i+1])
    return res

print(maxSum(arr))