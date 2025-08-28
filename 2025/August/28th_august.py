# Maximize Number of 1's

arr=[1,0,1]
k=1

def maxOnes(arr,k):
    n=len(arr)
    left=0
    zeroCount=0
    maxCount=0
    for right in range(n):
        if arr[right]==0:
            zeroCount+=1
        while zeroCount>k:
            if arr[left]==0:
                zeroCount-=1
            left+=1
        maxCount=max(maxCount,right-left+1)
    return maxCount

print(maxOnes(arr,k))