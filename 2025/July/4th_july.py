# Subarrays with At Most K Distinct Integers

arr=[1,2,2,3]
k=2

def subarraysWithAtMostKDistinct(arr, k):
    from collections import defaultdict
    n = len(arr)
    left = 0
    count = defaultdict(int)
    result = 0
    
    for right in range(n):
        count[arr[right]] += 1
        
        while len(count) > k:
            count[arr[left]] -= 1
            if count[arr[left]] == 0:
                del count[arr[left]]
            left += 1
        
        result += right - left + 1
    
    return result
print(subarraysWithAtMostKDistinct(arr, k))