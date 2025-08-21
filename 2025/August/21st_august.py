# Maximize the Minimum Difference between k elements

arr=[2,6,2,5]
k=3

def maxMinDiff(arr,k):
    def canPart(diff,arr,k,length):
        prev=arr[0]
        taken=1
        for i in range(1,length,1):
            if arr[i] - prev >= diff:
                taken += 1
                prev = arr[i]
                if taken >= k:
                    return True
        return False
    
    arr.sort()
    length=len(arr)
    start=0
    end=arr[-1] - arr[0]
    ans=-1
    while start<=end:
        mid=start+(end-start)//2
        if canPart(mid,arr,k,length):
            ans=max(ans,mid)
            start=mid+1
        else:
            end=mid-1
    return ans

print(maxMinDiff(arr, k))