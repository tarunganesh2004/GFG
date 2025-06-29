# Split Array Largest Sum 

arr=[1,2,3,4]
k=3

def splitArray(nums,k):
    mn=max(nums)
    mx=sum(nums)
    res=-1
    while mn<=mx:
        mid= (mn + mx) // 2
        cnt=1
        curr_sum=0
        for i in nums:
            if curr_sum + i > mid:
                cnt += 1
                curr_sum = i
            else:
                curr_sum += i
        if cnt <= k:
            res = mid  # noqa: F841
            mx = mid - 1
        else:
            mn = mid + 1
    return mn 

print(splitArray(arr, k))  # Output: 4