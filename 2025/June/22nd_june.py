# Largest Divisible Subset

arr=[1,16,7,8,4]

class Solution:
    def largestSubset(self, arr):
        # Sort array to maintain divisibility order (smaller elements first)
        arr.sort()
        n = len(arr)

        # Track the starting index and length of the longest subset found
        idx, l = n - 1, 1  # noqa: E741

        # dp[i] stores (length of longest subset starting at i, next element's index)
        # Initialize each position as a subset of length 1 with no next element
        dp = [(1, None) for _ in range(n)]

        # Process elements backwards from last to first
        for i in range(n - 1, -1, -1):
            li, k = dp[i]  # Current best length and next index at position i

            # Check all elements that come after position i
            for j in range(i + 1, n):
                # If arr[j] is divisible by arr[i], we can extend our chain
                if arr[j] % arr[i] == 0:
                    # If extending to j gives us a better or equal chain, update
                    if dp[j][0] + 1 >= li:
                        li = dp[j][0] + 1  # New chain length
                        k=j # next element in chain
            dp[i] = (li, k) # type: ignore # store the best chain info for position i 

        # Find the maximum length and its starting index
        if li>l:
            l = li  # noqa: E741
            idx = i
        # Reconstruct the longest subset
        subset = []
        while idx is not None:
            subset.append(arr[idx])
            idx = dp[idx][1]

        return subset
    
solution = Solution()
print(solution.largestSubset(arr))  # Output: [1, 4, 8, 16]