# Bitonic Point


arr=[1,2,4,5,7,8,3]

def findBitonicPoint(arr):
    n=len(arr)
    for i in range(n+1):
        if arr[i]<arr[i+1]:
            pass 
        else:
            return arr[i]
        
    return -1

print(findBitonicPoint(arr))