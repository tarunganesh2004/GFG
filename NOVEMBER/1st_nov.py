# Swap and Maximize

arr=[4,2,1,8]

def swapAndMaximize(arr):
    n=len(arr)
    arr.sort() # 1,2,4,8
    l1=[]
    l,r=0,n-1
    while l<r:
        l1.append(arr[l])
        l1.append(arr[r])
        l,r=l+1,r-1

    s=0
    for i in range(1,len(l1)):
        print(l1[i],end=" ")
        print(l1[i-1])
        s+=abs(l1[i]-l1[i-1])
        print(s)
    s+=abs(l1[-1]-l1[0])
    return s
print(swapAndMaximize(arr))
