# Longest Subarray with Majority Greater than K 
# Given an array arr[] and an integer k, the task is to find the length of longest subarray 
# in which the count of elements greater than k is more than the count of elements less than or equal to k.

arr=[1,2,3,4,1]
k=2


def longestSubarray(arr,k):
    from collections import defaultdict

    sm=0
    res=0
    dc=defaultdict(int)
    dc[0]=-1

    for idx,num in enumerate(arr):
        sm+=1 if num>k else -1

        if sm>0:
            res=max(res,idx+1)

        else:
            if sm not in dc:
                dc[sm]=idx

            if sm-1 in dc:
                res=max(res,idx-dc[sm-1])

    return res

print(longestSubarray(arr,k)) # Output: 3