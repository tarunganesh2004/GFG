# Longest Subarray with sum K

arr=[10,5,2,7,1,-10]
k=15
# sliding window approach fails for array containing both positive and negative numbers because 
# the sum of elements in the array can be greater than k even if the subarray sum is equal to k
# so we use prefix sum approach
def longestSubarray(arr,k):
    # n=len(arr)
    prefix_sum_map={}
    cur_sum=0
    max_len=0

    for i, num in enumerate(arr):
        cur_sum+=num

        if cur_sum==k:
            max_len=i+1

        if cur_sum-k in prefix_sum_map:
            max_len=max(max_len,i-prefix_sum_map[cur_sum-k]) # if exists then subarray from (index of previous prefix+1) to current index is the subarray with sum k


        if cur_sum not in prefix_sum_map:
            prefix_sum_map[cur_sum]=i # store the index of prefix sum in the map

    return max_len

# def longestUsingSlidingWindow(arr,k):
#     start=0
#     cur_sum=0
#     max_len=0
#     for end in range(len(arr)):
#         cur_sum+=arr[end]
#         while cur_sum>k and start<=end:
#             cur_sum-=arr[start]
#             start+=1
#         if cur_sum==k:
#             max_len=max(max_len,end-start+1)
#     return max_len


print(longestSubarray(arr,k))