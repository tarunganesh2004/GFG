# Sorted and Rotated Minimum

def findMin(arr):
    l, r = 0, len(arr) - 1  # noqa: E741
    if arr[l] < arr[r]:
        return arr[l]
    while l <= r:
        mid = l + (r - l) // 2
        if mid < r and arr[mid] > arr[mid + 1]:
            return arr[mid + 1]
        if mid > l and arr[mid - 1] > arr[mid]:
            return arr[mid]
        if arr[mid] > arr[l]:
            l = mid + 1  # noqa: E741
        else:
            r = mid - 1
    return arr[l]

arr=[5,6,1,2,3,4]

print(findMin(arr))