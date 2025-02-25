# Histogram Max Rectangular Area

arr=[60,20,50,40,10,50,60]

def maxRectArea(arr):
    n=len(arr)
    maxArea=0
    st=[]
    for i in range(n+1):
        while st and (i==n or arr[st[-1]]>arr[i]):
            h=arr[st.pop()]
            if not st:
                w=i
            else:
                w=i-st[-1]-1
            maxArea=max(maxArea,h*w)
        st.append(i)

    return maxArea

print(maxRectArea(arr))  # 100