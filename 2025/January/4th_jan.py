# Count all triplets with given sum in sorted array 

# Given a sorted array arr[] and a target value, the task is to count triplets (i, j, k) of valid indices, such that arr[i] + arr[j] + arr[k] = target and i < j < k.

from collections import defaultdict


arr=[-3,-1,-1,0,1,2]
target=-2

# Approach 1: Brute Force

def countTripletsBrute(arr,target):
    n=len(arr)
    count=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==target:
                    count+=1
    return count

# Approach 2 using hashing

def countTripletsHashing(arr,target):
    count = 0
    m=defaultdict(int)
    for ele in arr:
        m[ele]+=1 
    for i in range(len(arr)):
        m[arr[i]]-=1 # reduce the count of current element
        for j in range(0,i):
            lookfor=target-arr[i]-arr[j]
            count+=m[lookfor]
    return count

# Approach 3: Using two pointer approach(extended to original 3 sum problem)
def countTriplets(arr,target):
    n=len(arr)
    count=0

    for i in range(n-2):
        l=i+1  # noqa: E741
        r=n-1
        while l<r:
            s=arr[i]+arr[l]+arr[r]
            if s<target:
                l+=1  # noqa: E741
            elif s>target:
                r-=1
            else:
                ele1=arr[l]
                ele2=arr[r]
                c1=0
                c2=0
                # count frequency of cur val at left
                while l<=r and arr[l]==ele1:
                    c1+=1
                    l+=1  # noqa: E741
                # count frequency of cur val at right
                while l<=r and arr[r]==ele2:
                    c2+=1
                    r-=1
                

                # if both elements are same then we need to count the number of ways to select 2 elements from c1+c2 elements
                if ele1==ele2:
                    count+=c1*(c1-1)//2
                else:
                    count+=(c1*c2)
    return count



print(countTripletsBrute(arr,target))

print(countTripletsHashing(arr,target))

print(countTriplets(arr,target))