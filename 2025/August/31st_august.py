# Container With Most Water

arr=[1,5,4,3]

def maxWater(arr):
    left,right=0,len(arr)-1
    maxArea=0

    while left<right:
        area=min(arr[left],arr[right])*(right-left)
        maxArea=max(maxArea,area)
        if arr[left]<arr[right]:
            left+=1
        else:
            right-=1
    return maxArea

print(maxWater(arr))