arr=[3,5,10,15,17,12,9]
k=4

def sumDiffPairs(arr,k):
    n=len(arr)
    arr.sort(reverse=True)
    res=0
    i=0
    while i<n-1:
        if arr[i]-arr[i+1]<k:
            res+=arr[i]+arr[i+1]
            i+=2
        else:
            i+=1
    return res