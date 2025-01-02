# Subarrays with sum K

arr=[10,2,-2,-20,10]
k=-10

# BruteForce
def bruteForce(arr,k):
    c=0
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum+=arr[j]
            if sum==k:
                c+=1
    return c

# Using Map
def countSubarrays(arr,k):
    count=0
    cur_sum=0
    map={0:1} # 0:1 means 0 sum has occured 1 time
    for i in range(len(arr)):
        cur_sum+=arr[i]
        if cur_sum-k in map:
            count+=map[cur_sum-k]
        map[cur_sum]=map.get(cur_sum,0)+1
    return count

print(bruteForce(arr,k))

print(countSubarrays(arr,k))