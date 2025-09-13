# Minimize the Heights II

k=2
arr=[1,5,8,10]

def getMinDiff(arr,n,k):
    arr.sort()
    ans=arr[n-1]-arr[0]
    small=arr[0]+k
    big=arr[n-1]-k
    if small>big:
        small,big=big,small
    for i in range(1,n-1):
        add=arr[i]+k
        sub=arr[i]-k
        if sub>=small or add<=big:
            continue
        if big-sub<=add-small:
            small=sub
        else:
            big=add
    return min(ans,big-small)

print(getMinDiff(arr,len(arr),k))