# Count Pairs divisible By K 

arr=[2,2,1,7,5,3]
k=4

def bruteForce(arr,k):
    n=len(arr)
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i]+arr[j])% k==0:
                ans+=1
    return ans

def optimized(arr,k):
    n=len(arr)
    mp={}
    ans=0
    for i in range(n):
        rem=arr[i]%k 
        need=(k-rem)%k 
        
        ans+=mp.get(need,0)
        mp[rem]=mp.get(rem,0)+1
    return ans

print(bruteForce(arr,k))
print(optimized(arr,k))