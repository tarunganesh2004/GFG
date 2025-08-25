# Maximize median after doing k operations

arr=[1,3,4,5]
k=3

def maximizeMedian(arr,k):
    def isPossible(arr,target,k):
        n=len(arr)
        if n%2==1:
            for i in range(n//2,n):
                if arr[i]<target:
                    k-=(target-arr[i])
        else:
            if arr[n//2]<target:
                k-=(target-arr[n//2])
                k-=(target-arr[n//2-1])
            else:
                k-=(2*target-(arr[n//2]+arr[n//2-1]))

            for i in range(n//2+1,n):
                if arr[i]<target:
                    k-=(target-arr[i])
        return k>=0
    
    arr.sort()
    n=len(arr)
    initialMedian=arr[n//2]
    if n%2==0:
        initialMedian+=arr[n//2-1]
        initialMedian//=2
    
    low=initialMedian
    high=initialMedian+k
    bestMedian=initialMedian

    while low<=high:
        mid=(low+high)//2
        if isPossible(arr,mid,k):
            bestMedian=mid
            low=mid+1
        else:
            high=mid-1
    return bestMedian

print(maximizeMedian(arr,k))