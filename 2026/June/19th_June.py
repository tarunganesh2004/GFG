# Equalize all prefix Sums

arr=[1,6,9,12]

def bruteForce(arr): # O(n^2*target)
    res=[]
    n=len(arr)
    def findMinCost(prefix):
        best=float('inf')
        for target in range(min(prefix),max(prefix)+1):
            cost=0
            for num in prefix:
                cost+=abs(num-target)
            best=min(best,cost)
        return best
    for i in range(n):
        prefix=arr[0:i+1]
        best_cost=findMinCost(prefix)
        res.append(best_cost)
    
    return res

def another(arr): # O(n^2)
    n=len(arr)
    ans=[]
    for i in range(n):
        pre=arr[0:i+1]
        n1=len(pre)
        median=pre[(n1-1)//2]
        cost=sum(abs(x-median) for x in pre)
        ans.append(cost)
    return ans

# optimized
# the minimum sum of absolute differences is achieved at the median
def optimalArray(arr):
    n=len(arr)    
    ps=[0]*n 
    ps[0]=arr[0]
    for i in range(1,n):
        ps[i]=ps[i-1]+arr[i]

    ans=[]

    # iterate every prefix 
    for i in range(n):
        # median idx for every prefix 
        k=i//2
        median=arr[k]
        if k>0:
            leftSum=ps[k-1] # sum of elements before median
        else:
            leftSum=0

        leftCount=k # number of elements to the left of median
        leftCost=leftCount*median-leftSum # 

        rightSum=ps[i]-ps[k] # sum of elements after median with current prefix
        rightCount=i-k # number of elements after median

        rightCost=rightSum-rightCount*median 

        ans.append(leftCost+rightCost)

    return ans

# O(1) space with recurrence relation
def optimalArraySpace(arr):
    n=len(arr)
    ans=[0]*n
    for i in range(1,n):
        ans[i]=ans[i-1]+arr[i]-arr[i//2]
    return ans

print(bruteForce(arr))
print(optimalArray(arr))