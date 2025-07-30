# Subarrays with Sum K

arr=[10,2,-2,-20,10]
k=-10

def cntSubArrays(arr,k):
    m={0:1}
    sum=0
    count=0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum-k in m:
            count+=m[sum-k]
        if sum in m:
            m[sum]+=1
        else:
            m[sum]=1
    return count

print(cntSubArrays(arr,k))