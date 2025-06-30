# Max Min Height


arr=[2,3,4,5,1]
k=2
w=2

def maxMinHeight(arr, k, w):
    n=len(arr)
    def check(mid):
        added=[0] * n
        total_add=0
        ops=0
        for i in range(n):
            if i>=w:
                total_add -= added[i - w]
            effective_height = arr[i] + total_add
            if effective_height<mid:
                dif= mid - effective_height
                if ops+ dif > k:
                    return False
                added[i] = dif
                total_add += dif
                ops += dif
        return True
    low= min(arr)
    high=low+k 
    res=low 
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res

print(maxMinHeight(arr, k, w))  # Output: 2