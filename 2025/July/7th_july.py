# Next Greater Element in Circular Array 

arr=[1,3,2,4]

def nextGreaterCircular(arr):
    n=len(arr)
    res=[-1]*n
    stack=[]

    for i in range(2*n-1,-1,-1):
        while stack and arr[stack[-1]]<= arr[i%n]:
            stack.pop()
        if i < n:
            if stack:
                res[i]= arr[stack[-1]]
        stack.append(i%n)
    return res
        

print(nextGreaterCircular(arr))