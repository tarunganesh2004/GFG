# Container with Most Water
# Given an array arr[] of non-negative integers, where each element arr[i] represents the height of the vertical lines, find the maximum amount of water that can be contained between any two lines, together with the x-axis.

# Note: In the case of a single vertical line it will not be able to hold water.

arr=[1,5,4,3] # 6 , 5 and 3 are 2 distance apart and min(5,3) * 2 = 6
# the amount of water is determined by the minimum of the two heights and the width between them
# area=width*height=min(arr[left],arr[right])*(right-left)

def maxWaterContainerBrute(arr): # O(n^2) TC, O(1) SC
    n=len(arr)
    maxWater=0
    for i in range(n):
        for j in range(i+1,n):
            maxWater=max(maxWater,min(arr[i],arr[j])*(j-i))
    return maxWater

def maxWaterContainerOptimized(arr): # O(n) TC, O(1) SC
    n=len(arr)
    left,right=0,n-1
    maxWater=0
    while left<right:
        maxWater=max(maxWater,min(arr[left],arr[right])*(right-left))
        if arr[left]<arr[right]:
            left+=1
        else:
            right-=1
    return maxWater

print(maxWaterContainerBrute(arr))
print(maxWaterContainerOptimized(arr))