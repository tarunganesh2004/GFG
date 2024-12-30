# Sort 0s,1s,2s

arr=[0,1,2,0,1,2,0,1,2]

def sort012s(arr):
    c0=0
    c1=0
    c2=0 
    for i in arr:
        if i==0:
            c0+=1
        elif i==1:
            c1+=1
        else:
            c2+=1

    for i in range(c0):
        arr[i]=0
    for i in range(c0,c0+c1):
        arr[i]=1
    for i in range(c0+c1,c0+c1+c2):
        arr[i]=2

    return arr

print(sort012s(arr))