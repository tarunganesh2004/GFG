# Missing Element of AP

arr=[2,4,8,10,12,14]

# brute force approach
def brute(arr):
    d=arr[1]-arr[0]
    n=len(arr)
    for i in range(n-1):
        if d!= arr[i+1]-arr[i]:
            return arr[i]+d
        
    return arr[-1]+d

def findMissing(arr):
    n = len(arr)
    # commmon difference last-first/n 
    diff = (arr[-1] - arr[0]) // n
    low,high= 0, n-1
    while low<high:
        mid= (low+high)//2
        expected= arr[0] + (mid * diff)
        if arr[mid] == expected:
            low = mid + 1
        else:
            high = mid
    
    return arr[0] + (low * diff)
    

print(findMissing(arr)) # Output: 6