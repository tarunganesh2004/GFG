# Indexes of Subarray sum
# find the continous subarray(1 based indexing) which sums to given sum, 
# we need to find the first subarray with sum equal to given sum

arr=[1,2,3,7,5]
sum=12 # [2,4] 2nd to 4th index(1 based indexing) 2+3+7=12

def brute(arr,target):
    n=len(arr)
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=arr[j]
            if s==target:
                return [i+1,j+1]
    return -1

# using sliding window O(n) & O(1)

def subarraySum(arr,target):
    n=len(arr)
    start=0
    cur_sum=0
    for end in range(n):
        cur_sum+=arr[end]
        while cur_sum>target:
            cur_sum-=arr[start]
            start+=1
        if cur_sum==target:
            return [start+1,end+1]
    return -1

# using prefix sums O(n) & O(n)
def find_subarray_prefix_sum(arr,target):
    prefix_sum={}
    cur_sum=0

    for i,num in enumerate(arr):
        cur_sum+=num
        if cur_sum==target:
            return [1 ,i+1] # 1 based indexing
        if cur_sum-target in prefix_sum:
            return [prefix_sum[cur_sum-target]+2,i+1] # 1 based indexing
        prefix_sum[cur_sum]=i

    return -1

print(brute(arr,sum)) # (2,4)
print(subarraySum(arr,sum)) # (2,4)