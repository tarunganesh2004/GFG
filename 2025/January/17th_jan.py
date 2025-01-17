# Product array puzzle

arr=[10,3,5,6,2]

# brute force
def bruteForce(arr):
    res=[1]*len(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j:
                res[i]*=arr[j]

    return res

# using prefix and suffix arrays
def productArray(arr): # O(n) time and space
    n=len(arr)
    prefix=[1]*n
    suffix=[1]*n
    for i in range(1,n):
        prefix[i]=prefix[i-1]*arr[i-1]
    for i in range(n-2,-1,-1):
        suffix[i]=suffix[i+1]*arr[i+1]
    res=[1]*n
    for i in range(n):
        res[i]=prefix[i]*suffix[i]
    return res


def productExceptSelfAnotherApproach(arr):
    n=len(arr)
    res=[1]*n
    for i in range(1,n):
        res[i]=res[i-1]*arr[i-1]
    right=1
    for i in range(n-1,-1,-1):
        res[i]*=right
        right*=arr[i]
    return res

# optimized O(1) space
def optimized(arr):
    n=len(arr)
    # handle zeroes, count zeroes and their index
    # if array contains more than one zero,entire array product will be 0
    # if array contains only one zero, except that index all other elements will be 0
    total_product=1
    zero_count=0
    for num in arr:
        if num==0:
            zero_count+=1
        else:
            total_product*=num

    res=[0]*n
    if zero_count>1:
        return res
    for i in range(n):
        if zero_count==1:
            if arr[i]==0:
                res[i]=total_product
            else:
                res[i]=0
        else:
            res[i]=total_product//arr[i]
    return res



print(bruteForce(arr))
print(productArray(arr))
print(productExceptSelfAnotherApproach(arr))
print(optimized(arr))