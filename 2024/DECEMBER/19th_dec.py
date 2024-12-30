# Kth Missing Positive Number in Sorted Array

arr=[2,3,4,7,11] # 1,5,6,8,9,10,12.......
k=5

def kthMissingBrute(arr,k):
    count=0
    i=0
    while count!=k:
        i+=1
        if i not in arr:
            count+=1
            if count==k:
                return i
    return -1

def bruteForceAnother(arr,k):
    for i in range(len(arr)):
        if arr[i]<=k:
            k+=1
        else:
            break
    return k
            
# The other Approach is to use Binary Search O(logn)
def kthMissingPositive(arr,k):
    n=len(arr) # formula for missing element at each index i is arr[i]-(i+1)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        missing=arr[mid]-(mid+1)
        if missing<k:
            low=mid+1
        else:
            high=mid-1
        # now printing the missing element
        # arr[high]- more, i.e more is missing-k
        # arr[high]-(missing-k) ==> arr[high]-(arr[high]-(high+1)-k)
        # high+1+k
    return high+1+k # or low=high+1, return low+k

print(kthMissingBrute(arr,k))
print(bruteForceAnother(arr,k))
print(kthMissingPositive(arr,k))