# Farthest smaller right 

arr=[2,5,1,3,2]

def bruteForce(arr): # O(n^2) solution
    res=[]
    for i in range(len(arr)):
        farthest=-1
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                farthest = j
        res.append(farthest)
    return res


# Optimized solution using Binary Search
def optimized(arr): # O(n log n) solution
    # using suffix minimum 
    n=len(arr)
    ans=[-1]*n
    suffix_min = [0] * n
    suffix_min[n-1] = arr[n-1]

    for i in range(n-2, -1, -1):
        suffix_min[i] = min(suffix_min[i+1], arr[i])
    for i in range(n):
        low,high= i+1, n-1
        res=-1
        while low<=high:
            mid= (low + high) // 2
            if suffix_min[mid]<arr[i]:
                res=mid
                low=mid+1
            else:
                high=mid-1
        ans[i]=res
    return ans


print(bruteForce(arr))
print(optimized(arr))