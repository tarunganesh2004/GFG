# Equilibrium Point

arr=[1,2,0,3]
arr1=[-7,1,5,2,-4,3,0]

def equilibriumPoint(arr): # O(n) & O(1)
    n=len(arr)
    total_sum=sum(arr)
    left_sum=0
    for i in range(n):
        total_sum-=arr[i]
        if left_sum==total_sum:
            return i
        left_sum+=arr[i]
    return -1

print(equilibriumPoint(arr))
print(equilibriumPoint(arr1))