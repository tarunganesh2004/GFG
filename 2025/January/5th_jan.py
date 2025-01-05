# Count pairs whose sum is less than target

arr=[7,2,5,3]
target=8

def countPairs(arr,target):
    arr.sort()
    n=len(arr)
    left=0
    right=n-1
    count=0
    while left<right:
        if arr[left]+arr[right]<target:
            count+=right-left
            left+=1
        else:
            right-=1
    return count

print(countPairs(arr,target))