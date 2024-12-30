# Allocate Minimum Pages

arr=[12,34,67,90]
students=2

def isPossible(arr,n,m,k):
    studentsRequired=1
    sum1=0
    for i in range(n):
        if arr[i]>m:
            return False
        if sum1+arr[i]>m:
            studentsRequired+=1
            sum1=arr[i]
            if studentsRequired>k:
                return False
        else:
            sum1+=arr[i]
    return True

def allocate(arr,n,k):
    low=max(arr)
    high=sum(arr)
    res=-1
    while low<=high:
        mid=(low+high)//2
        if isPossible(arr,n,mid,k):
            res=mid
            high=mid-1
        else:
            low=mid+1
    return res

print(allocate(arr,len(arr),students))