# rotate to right(clock wise)

arr=[1,2,3,4,5] # 3,4,5,1,2
d=2
def rotate(arr,d):
    n=len(arr)
    d=d%n
    l1=arr[:d]
    l2=arr[d:]
    arr[:]=l2+l1
    return arr

print(rotate(arr,d))