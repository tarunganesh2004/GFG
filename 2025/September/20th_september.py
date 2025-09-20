# Longest Subarray Length
# longest subarray such that elements of the subarray 
# are smaller than or equal to the length of the subarray

arr=[1,2,3]

def longestSubarray(arr):
    n=len(arr)
    left,right=[-1]*n,[n]*n

    stack=[]
    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]]<=arr[i]:
            stack.pop()
        if stack:
            right[i]=stack[-1]
        stack.append(i)

    stack=[]
    for i in range(n):
        while stack and arr[stack[-1]]<=arr[i]:
            stack.pop()
        if stack:
            left[i]=stack[-1]
        stack.append(i)
    max_length=0
    for i in range(n):
        length=right[i]-left[i]-1
        if arr[i]>length:
            continue
        max_length=max(max_length,length)
    return max_length

print(longestSubarray(arr))