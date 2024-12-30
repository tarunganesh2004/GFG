# Count Inversions


class Solution:
    def mergeSort(self, arr, low, high):
        count = 0
        if low >= high:
            return count
        mid = (low + high) // 2

        count += self.mergeSort(arr, low, mid)
        count += self.mergeSort(arr, mid + 1, high)
        count += self.merge(arr, low, mid, high)
        return count

    def merge(self, arr, low, mid, high):
        left = low
        right = mid + 1
        temp = []
        count = 0

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                count += mid - left + 1  # Count inversions
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy the sorted temp array back into the original array
        for i in range(len(temp)):
            arr[low + i] = temp[i]
        return count

    def inversionCount(self, arr):
        # Entry point for counting inversions
        n = len(arr)
        c = self.mergeSort(arr, 0, n - 1)  # Add self. to call mergeSort
        return c

arr=[2, 4, 1, 3, 5]
sol=Solution()
print(sol.inversionCount(arr))