# kadane's algorithm

arr=[2,3,-8,7,-1,2,3]

def kadane(arr):
    n=len(arr)
    max_so_far=arr[0]
    max_ending_here=arr[0]
    for i in range(1,n):
        max_ending_here=max(arr[i],max_ending_here+arr[i])
        max_so_far=max(max_so_far,max_ending_here)

    return max_so_far

def anotherApproach(arr):
    n=len(arr)
    sum=0
    max_sum=float('-inf')
    for i in range(n):
        sum+=arr[i]
        if sum>max_sum:
            max_sum=sum
        if sum<0:
            sum=0
    return max_sum

print(kadane(arr))
print(anotherApproach(arr))