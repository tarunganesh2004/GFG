# Stock Span Problem

arr=[100, 80, 60, 70, 60, 75, 85]

def stockSpan(arr):
    st=[]
    res=[0]*len(arr)

    for i in range(len(arr)):
        while st and arr[st[-1]]<=arr[i]:
            st.pop()
        res[i]=i-st[-1] if st else i+1
        st.append(i)
    return res

print(stockSpan(arr))  # [1, 1, 1, 2, 1, 4, 6]