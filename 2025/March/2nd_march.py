# K Sized Subarray Maximum

arr=[1,2,3,1,4,5,2,3,6]
k=3

# brute force
def bruteForce(arr,k):
    res=[]
    for i in range(len(arr)-k+1):
        res.append(max(arr[i:i+k]))
    return res

print(bruteForce(arr,k))