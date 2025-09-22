# Max of Min for every Window size

arr=[10,20,30,50,10,70,30]

def max_of_min(arr):
    n=len(arr)
    left=[-1]*n
    right=[n]*n

    # next smaller element on left
    stack=[]
    for i in range(n):
        while stack and arr[stack[-1]]>=arr[i]:
            stack.pop()
        if stack:
            left[i]=stack[-1]
        stack.append(i)

    # next smaller element on right
    stack=[]
    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]]>=arr[i]:
            stack.pop()
        if stack:
            right[i]=stack[-1]
        stack.append(i)

    # length of window in which arr[i] is minimum
    length=[0]*n
    for i in range(n):
        length[i]=right[i]-left[i]-1

    # ans array to store max of min for every window size
    ans=[0]*(n+1)
    for i in range(n):
        ans[length[i]]=max(ans[length[i]],arr[i])

    # fill the rest of the entries
    for i in range(n-1,0,-1):
        ans[i]=max(ans[i],ans[i+1])

    return ans[1:] # ignoring 0th index as window size starts from 1

print(max_of_min(arr))