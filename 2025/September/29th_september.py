# Maximum Subarray sum 2

arr=[4,5,-1,-2,6]
a=2
b=4

def maxSubarrSum(arr,a,b):
    from collections import deque
    n=len(arr)
    pre_sum=[0]*(n+1)
    for i in range(n):
        pre_sum[i+1]=pre_sum[i]+arr[i]
    
    dq=deque()
    ans=float('-inf')
    for r in range(a,n+1):
        while dq and pre_sum[dq[-1]]>=pre_sum[r-a]:
            dq.pop()
        dq.append(r-a)

        while dq and dq[0]<r-b:
            dq.popleft()
        ans=max(ans,pre_sum[r]-pre_sum[dq[0]])
    return ans

print(maxSubarrSum(arr,a,b))