# Number Of Occurance

arr=[1,1,2,2,2,2,3]
x=2

class Solution:
    def countFreq(self, arr, target):
        # Find the first occurrence of the target
        first_occurrence = self.firstOccurrence(arr, target)

        # If the target is not found, return 0
        if first_occurrence == -1:
            return 0

        # Find the last occurrence of the target
        last_occurrence = self.lastOccurrence(arr, target)

        # Return the count of the target
        return last_occurrence - first_occurrence + 1

    def firstOccurrence(self, arr, target):
        # Find the first occurrence of the target
        n = len(arr)
        low, high = 0, n - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                ans = mid
                high = mid - 1  # Move left to find the first occurrence
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def lastOccurrence(self, arr, target):
        # Find the last occurrence of the target
        n = len(arr)
        low, high = 0, n - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                ans = mid
                low = mid + 1  # Move right to find the last occurrence
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans

sol=Solution()
print(sol.countFreq(arr,x))