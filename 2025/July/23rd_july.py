# Sum of subarrays

arr=[1,2,3]

# brute force
def sumOfSubarraysBrute(arr):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        for j in range(i, n):
            total_sum += sum(arr[i:j+1])
    return total_sum

# optimized
def sumOfSubarraysOptimal(arr):
    n= len(arr)
    total_sum = 0
    for i in range(n):
        total_sum += arr[i] * (i + 1) * (n - i)
    return total_sum

print(sumOfSubarraysBrute(arr))
print(sumOfSubarraysOptimal(arr))