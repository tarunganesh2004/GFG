# Maximum of Minimum for every window size

arr=[10,20,30,50,10,70,30]

def maxMin(arr):
    n=len(arr)
    left=[-1]*n
    right=[n]*n
    st=[]
    for i in range(n):
        while st and arr[st[-1]]>=arr[i]:
            st.pop()
        if st:
            left[i]=st[-1]
        st.append(i)
    st=[]
    for i in range(n-1,-1,-1):
        while st and arr[st[-1]]>=arr[i]:
            st.pop()
        if st:
            right[i]=st[-1]
        st.append(i)
    print(left)
    print(right)
    ans=[0]*(n+1)
    for i in range(n):
        l=right[i]-left[i]-1  # noqa: E741
        ans[l]=max(ans[l],arr[i])
    for i in range(n-1,0,-1):
        ans[i]=max(ans[i],ans[i+1])
    return ans[1:]

print(maxMin(arr))  # [70, 50, 30, 20, 10, 10, 10]