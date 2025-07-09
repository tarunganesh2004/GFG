# Sum of subarray minimum

arr=[3,1,2,4]

# brute force
def bruteForce(arr):
    n=len(arr)
    total=0
    for i in range(n):
        min_val = arr[i]
        for j in range(i, n):
            min_val = min(min_val, arr[j])
            total += min_val
    return total

# optimized
def optimized(arr):
    n = len(arr)
    stack = []

    # Previous Less Element count
    ple = [0] * n
    for i in range(n):
        count = 1
        while stack and stack[-1][0] > arr[i]:
            count += stack.pop()[1]
        ple[i] = count
        stack.append((arr[i], count))

    stack = []

    # Next Less Element count
    nle = [0] * n
    for i in range(n - 1, -1, -1):
        count = 1
        while stack and stack[-1][0] >= arr[i]:
            count += stack.pop()[1]
        nle[i] = count
        stack.append((arr[i], count))

    # Total sum
    total = 0
    for i in range(n):
        total += arr[i] * ple[i] * nle[i]
    return total


print(bruteForce(arr))

print(optimized(arr))