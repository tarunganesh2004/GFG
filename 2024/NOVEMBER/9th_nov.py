# Minimum Sum
# https://www.geeksforgeeks.org/problems/minimum-sum4058/1

arr=[6,8,4,5,2,3]

def minSum(arr):
    arr.sort()
    n=len(arr)
    m=n//2

    s