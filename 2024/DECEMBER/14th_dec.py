# Search in a rotated sorted array

arr=[5,6,7,8,9,10,1,2,3]
key=3

class Solution:
    def search(self, arr, key):
        # Complete this function
        l, r = 0, len(arr) - 1  # noqa: E741
        ll = len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mid < r and arr[mid] > arr[mid + 1]:
                ll = mid
                break
            if mid > l and arr[mid - 1] > arr[mid]:
                ll = mid - 1
                break
            if arr[mid] > arr[l]:
                l = mid + 1  # noqa: E741
            else:
                r = mid - 1

        def helper(l, r):  # noqa: E741
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == key:
                    return mid
                elif arr[mid] > key:
                    r = mid - 1
                else:
                    l = mid + 1  # noqa: E741
            return -1

        f1 = helper(0, ll)
        f2 = helper(ll + 1, len(arr) - 1)
        if f1 != -1:
            return f1
        elif f2 != -1:
            return f2
        return -1
    
sol=Solution()
print(sol.search(arr,key))