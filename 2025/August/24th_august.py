# Minimum Days to Make M bouquets

m=3
k=2
arr=[3,4,2,7,13,8,5]

def minDaysBloom(arr,k,m):
    n=len(arr)
    if m*k>n:
        return -1

    def canMake(day):
        bouquets = 0
        flowers = 0
        for i in range(n):
            if arr[i] <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m
    
    left,right=min(arr),max(arr)
    result=-1
    while left<=right:
        mid=(left+right)//2
        if canMake(mid):
            result=mid
            right=mid-1
        else:
            left=mid+1
    return result

print(minDaysBloom(arr,k,m))