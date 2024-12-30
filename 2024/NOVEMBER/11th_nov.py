# Make array elements unique
# https://www.geeksforgeeks.org/problems/make-array-elements-unique--170645/1

arr=[1,2,2]
arr1=[1,1,2,3]
arr2=[5,4,3,2,1]
def minIncrements(arr):
    arr.sort()
    print(arr)
    n=len(arr)

    operations=0

    for i in range(1,n):
        if arr[i]<=arr[i-1]:
            k=arr[i-1]+1-arr[i]
            print(k)
            arr[i]+=k
            print(arr)
            operations+=k
            print(operations)
    return operations

print(minIncrements(arr1))
print(minIncrements(arr2))