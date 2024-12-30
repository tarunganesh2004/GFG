# Aggressive cows

def check(mid, arr, n, c):
    cows = 1
    pos = arr[0]
    for i in range(1, n):
        if arr[i] - pos >= mid:
            pos = arr[i]
            cows += 1
            if cows == c:
                return True
    return False

def aggressive_cows(arr, n, c):
    arr.sort()
    low = 1
    high = arr[n - 1] - arr[0]
    res = -1
    while low < high:
        mid = (low + high) // 2
        if check(mid, arr, n, c):
            res = mid
            low = mid + 1
        else:
            high = mid
    return res

arr = [1, 2, 4, 8, 9]
n = len(arr)
c = 3
print(aggressive_cows(arr, n, c))