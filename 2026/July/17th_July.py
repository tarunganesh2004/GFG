# Max Absolute diff of two subarrays

arr=[-2,-3,4,-1,-2,1,5,-3]

# brute force
def brute_force(arr): # TLE
    n=len(arr)
    ans=0

    # 1st subarray
    for l1 in range(n):
        for r1 in range(l1,n):

            # 2nd subarray
            for l2 in range(r1+1,n):
                for r2 in range(l2,n):

                    # # should not overlap
                    # if r1>l2 or l1>r2:
                    #     continue

                    s1=0 # here to compute sums , we can use prefix sums 
                    for i in range(l1,r1+1):
                        s1+=arr[i]
                    s2=0
                    for i in range(l2,r2+1):
                        s2+=arr[i]

                    diff=abs(s1-s2)
                    ans=max(ans,diff)
    return ans


# optimized
"""
max(a-b)=max(a-min(b),max(b)-a)
so for a fixed sum1, ans=max(sum1-min_sum2,max_sum2=sum1)

now we can split (since they asked for non overlapping subarrays)
left | right  ==> max(abs(leftSum-rightSum))

instead of computing every left sum with right sum,
we know the maximum absolute difference comes from opposite extremes
so max(abs(left_sum-right_sum)) becomes 
max(
    leftMax - rightMin,
    rightMax - leftMin
)

so for left side: find min subarray sum,max subarray sum
same for right side : find min subarray sum,max subarray sum 
so for each boundary left | right
we need leftMax-rightMin, rightMax-leftMin

so for every possible split:
    find:
        leftMax
        leftMin
        rightMax
        rightMin
    candidate = max(
        leftMax - rightMin,
        rightMax - leftMin
    )
    answer = max(answer, candidate)

so to compute these 4 values efficiently for every split we use kadane 
leftMax[i] -->Maximum sum of any subarray completely inside arr[0...i].

"""
def max_absolute_diff(arr):
    n=len(arr)

    left_max=[0]*n 
    left_min=[0]*n 
    right_max=[0]*n 
    right_min=[0]*n 

    # 1. max subarray sum for every prefix(left)
    cur=arr[0]
    best=arr[0]
    left_max[0]=best 
    for i in range(1,n):
        cur=max(arr[i],cur+arr[i])
        best=max(best,cur)

        left_max[i]=best 

    # 2. min subarray sum for every prefix
    cur=arr[0]
    best=arr[0]
    left_min[0]=best 
    for i in range(1,n):
        cur=min(arr[i],arr[i]+cur)
        best=min(best,cur)

        left_min[i]=best
    
    # right part(suffix)
    # 3. max subarray sum for every suffix
    cur=arr[n-1]
    best=arr[n-1]
    right_max[n-1]=best 
    for i in range(n-2,-1,-1):
        cur=max(arr[i],cur+arr[i])
        best=max(best,cur)

        right_max[i]=best 

    # 4. min subarray sum for every suffix
    cur=arr[n-1]
    best=arr[n-1]
    right_min[n-1]=best 
    for i in range(n-2,-1,-1):
        cur=min(arr[i],cur+arr[i])
        best=min(best,cur)

        right_min[i]=best 

    # try everysplit
    ans=0
    for i in range(n-1):
        candidate=max(left_max[i]-right_min[i+1],right_max[i+1]-left_min[i])
        ans=max(ans,candidate)
    return ans 

print(brute_force(arr))

print(max_absolute_diff(arr))

"""
Two non-overlapping subarrays
            ↓
There is a split between them
            ↓
For every split:
    left portion | right portion
            ↓
Need extreme subarray sums
            ↓
left maximum, left minimum
right maximum, right minimum
            ↓
Maximum subarray = Kadane
Minimum subarray = reverse Kadane logic
            ↓
Prefix arrays + suffix arrays
            ↓
Check every split
"""
