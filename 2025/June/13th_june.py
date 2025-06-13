# Koko Eating Bananas

arr=[3,6,7,11]
k=8

def kokoEat(arr,k):
    def canEat(mid):
        total = 0
        for i in arr:
            total += (i + mid - 1) // mid  # Equivalent to ceil(i / mid)
        return total <= k

    low, high = 1, max(arr)
    while low < high:
        mid = (low + high) // 2
        if canEat(mid):
            high = mid
        else:
            low = mid + 1
    return low

print(kokoEat(arr, k))  # Output: 4