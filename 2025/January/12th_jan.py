# Trapping Rain Water

arr=[3, 0, 1, 0, 4, 0 ,2]

# the idea is summation of (min(leftMaxBuilding,rightMax)-arr[i]) ==> total units of water
# so we should find leftmax and rightmax
# instead of doing those we can use prefixMax and suffixMax

def trappingRainWater(arr): # O(3N) TC, O(2N) -> SC 
    n=len(arr)
    prefixMax=[0]*n
    prefixMax[0]=arr[0]
    for i in range(1,n):
        prefixMax[i]=max(prefixMax[i-1],arr[i])
    
    suffixMax=[0]*n
    suffixMax[n-1]=arr[n-1]
    for i in range(n-2,0,-1):
        suffixMax[i]=max(suffixMax[i+1],arr[i])
    
    total=0
    for i in range(n):
        leftMax=prefixMax[i]
        rightMax=suffixMax[i]
        if arr[i]<leftMax and arr[i]<rightMax:
            total+=(min(leftMax,rightMax)-arr[i])
    return total

def spaceOptimizedApproach(arr): # O(n) & O(1)
    # using two pointers
    n=len(arr)
    left,right=0,n-1
    leftMax,rightMax=0,0
    total=0
    
    while left<=right:
        if arr[left]<=arr[right]:
            if arr[left]<leftMax:
                total+=leftMax-arr[left]
            else:
                leftMax=arr[left]
            left+=1
        else:
            if arr[right]<rightMax:
                total+=rightMax-arr[right]
            else:
                rightMax=arr[right]
            right-=1

    return total


print(trappingRainWater(arr))