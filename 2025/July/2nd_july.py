# Longest Subarray withatmost two distinct integers

arr=[2,1,2]

# brute force
def bruteForce(arr):
    n=len(arr)
    max_length = 0
    for i in range(n):
        distinct = set()
        for j in range(i, n):
            distinct.add(arr[j])
            if len(distinct) <= 2:
                max_length = max(max_length, j - i + 1)
            else:
                break
    return max_length

# optimized Sliding Window
def optimized(arr):
    from collections import defaultdict
    n=len(arr)
    left=0
    max_len=0
    count=defaultdict(int)
    for right in range(n):
        count[arr[right]]+=1

        while len(count)>2:
            count[arr[left]]-=1
            if count[arr[left]]==0:
                del count[arr[left]]
            left+=1
        max_len=max(max_len, right-left+1)
    return max_len
    

print(bruteForce(arr))
print(optimized(arr))