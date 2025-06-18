# Coin Piles


arr=[2,2,2,2]
k=0

def minimumCoins(arr,k):
    from bisect import bisect_right  # noqa: F401
    import bisect
    arr.sort()
    n=len(arr)

    prefix=[0]*n
    prefix[0]=arr[0]
    for i in range(1,n):
        prefix[i]=prefix[i-1]+arr[i]

    ans=float('inf')
    prev=0
    for i in range(n):
        if i>0 and arr[i] == arr[i-1]:
            continue
        if i>0:
            prev=prefix[i-1]

        pos=bisect.bisect_right(arr, arr[i] + k,i,n)
        
        totalToRemove=prev 

        if pos<n:
            totalToRemove += prefix[n-1] - prefix[pos-1]- (n-pos) *(arr[i] + k)


        ans=min(ans, totalToRemove)
    return ans

print(minimumCoins(arr, k))