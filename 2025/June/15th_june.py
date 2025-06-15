# Smallest Divisor

arr=[1, 2, 5, 9]
k=6

def smallestDivisor(nums, k):
    def isValid(divisor):
        total = sum((num + divisor - 1) // divisor for num in nums)
        return total <= k

    left, right = 1, max(nums)
    while left < right:
        mid = (left + right) // 2
        if isValid(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(smallestDivisor(arr, k))  # Output: 5