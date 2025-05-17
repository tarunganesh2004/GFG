# # Sort the given array after applying the given equation

# Given an integer array arr[] sorted in ascending order, along with three integers: A, B, and C. The task is to transform each element x in the array using the quadratic function A*(x2) + B*x + C. After applying this transformation to every element, return the modified array in sorted order.


arr=[-4,-2,0,2,4]
A=1
B=3
C=5

def sortTransformedArray(arr, A, B, C):
    n=len(arr)
    # equation
    def equation(x):
        return A * (x ** 2) + B * x + C
    
    transformed= [0] * n
    for i in range(n):
        transformed[i] = equation(arr[i])

    # Sort the transformed array
    transformed.sort()

    return transformed

print(sortTransformedArray(arr, A, B, C))