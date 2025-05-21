# Kth Smallest Number in Multiplication Table

m=3
n=3
k=5


# brute force
def kthSmallestBrute(m,n,k):
    arr=[]
    for i in range(1,m+1):
        for j in range(1,n+1):
            arr.append(i*j)
    arr.sort()
    return arr[k-1]

# binary search
def kthSmallest(m,n,k):
    def count(val,m,n):
        count=0
        for i in range(1,m+1):
            count+=min(val//i,n)
        return count
    
    low,high=1,m*n
    while low<high:
        mid=(low+high)//2
        if count(mid,m,n)<k:
            low=mid+1
        else:
            high=mid
    return low

print(kthSmallestBrute(m,n,k))
print(kthSmallest(m,n,k))