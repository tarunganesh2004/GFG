# Minimum Jumps

arr=[1,3,5,8,9,2,6,7,6,8,9]

def minJumps(arr):
    n=len(arr)
    if n==0 or arr[0]==0:
        return -1 
    if n==1:
        return 0
    jumps,curEnd,farthest=0,0,0
    for i in range(n-1):
        farthest=max(farthest,i+arr[i])
        if i==curEnd:
            jumps+=1
            curEnd=farthest
            if curEnd>=n-1:
                return jumps
    return -1

print(minJumps(arr))
