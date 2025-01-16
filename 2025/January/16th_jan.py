# Largest subarray of 0's and 1's

arr=[1,0,1,1,1,0,0]

# brute force approach

def bruteForce(arr): # O(n^2)
    n=len(arr)
    max_len=0
    for i in range(n):
        count0=0
        count1=0
        for j in range(i,n):
            if arr[j]==0:
                count0+=1
            else:
                count1+=1
            if count0==count1:
                max_len=max(max_len,j-i+1)
    return max_len

# using hashmap and prefix sum approach(0->-1, 1->1)
# we should find the subarray with sum 0
def largestSubarray(arr): # O(n)
    n=len(arr)
    max_len=0
    map={}
    pre_sum=0
    for i in range(n):
        pre_sum+=-1 if arr[i]==0 else 1
        if pre_sum==0:
            max_len=i+1
        if pre_sum in map:
            max_len=max(max_len,i-map[pre_sum])
        if pre_sum not in map:
            map[pre_sum]=i

    return max_len

print(bruteForce(arr))

print(largestSubarray(arr))