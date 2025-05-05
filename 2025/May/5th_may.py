# Search in an almolt sorted array



arr=[10,3,40,20,50,80,70,60]
target=40

def search(arr, x):
    n=len(arr)
    for i in range(n):
        if arr[i]==x:
            return i
    return -1

#using binary search
def binary_search(arr,x):
    left,right =0,len(arr)-1  # noqa: F811
    while right>=left:
        mid=left+(right-left)//2
        if arr[mid]==x:
            return mid
        if mid>left and arr[mid-1]==x:
            return mid-1
        if mid<right and arr[mid+1]==x:
            return mid+1
        
        if arr[mid]>x:
            right=mid-2
        else:
            left=mid+2

    return -1
    

print(search(arr, target)) # Output: 2
print(binary_search(arr, target)) # Output: 2
