# Smallest Non Zero Number

arr=[3,4,3,2,4]

# brute force
def bruteForce(arr):
    x=0

    def survives(start,arr):
        x=start
        for num in arr:
            if x>num:
                x+=(x-num)
            else:
                x-=(num-x)
            
            if x<0:
                return False
        return True
    while True:
        if survives(x,arr):
            return x 
        x+=1
    return x

# another approach is to use binary search 
def find(arr):
    
    def survives(start,arr):
        x=start 
        for num in arr:
            x=2*x-num 
            if x<0:
                return False
        return True 
    
    low=0
    high=max(arr)
    ans=high 

    while low<=high:
        mid=(low+high)//2
        if survives(mid,arr):
            ans=mid 
            high=mid-1
        else:
            low=mid+1
    return ans 

# optimized
def smallestX(arr):
    need=0
    for i in range(len(arr)-1,-1,-1):
        need=(need+arr[i]+1)//2
    return need

print(bruteForce(arr))
print(find(arr))
print(smallestX(arr))