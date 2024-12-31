# Maximum product subarray

arr=[-2,6,-3,-10,0,2]

def maxProductSubarray(arr):
    if not arr:
        return 0
    n=len(arr)
    cur_max=arr[0]
    cur_min=arr[0]
    result=arr[0]

    for i in range(1,n):
        if arr[i]<0: # if negative, swap max and min
            cur_max,cur_min=cur_min,cur_max

        cur_max=max(arr[i],cur_max*arr[i]) 
        cur_min=min(arr[i],cur_min*arr[i])

        result=max(result,cur_max)

    return result

print(maxProductSubarray(arr))