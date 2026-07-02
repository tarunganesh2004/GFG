# Check Subset Sum divisible by k

arr=[3,1,7,5]
k=6

"""
General approach is recursion with states f(i,sum)
def f(i, sm):
    if i == n:
        return sm > 0 and sm % k == 0

    take = f(i+1, sm+arr[i])
    notTake = f(i+1, sm)

    return take or notTake

now let k=5,and current sum=17 to know divisibility we dont want 17, we can do 17%5=2
so we dont care about sum, we can only care about remainder(sum%k)

so recurrence becomes f(i,rem)
f(i, rem):

    take = f(i+1, (rem + arr[i]) % k) 

    notTake = f(i+1, rem)

    return take or notTake

but here in the problem we want non empty subset
so we must also know whether we picked anything
so state becomes f(i,rem,taken)
"""

# recursion 
def recursion(arr,k):
    n=len(arr)
    # taken=0 --> no element choosen yet, taken=1 --> atleast one element choosen
    def f(i,rem,taken):
        if i==n:
            return rem==0 and taken
        
        take=f(i+1,(rem+arr[i])%k,True)
        # skip current element, but preserve taken state
        notTake=f(i+1,rem,taken)

        return take or notTake
    
    return f(0,0,False)

# memoization
def memoization(arr,k):
    n=len(arr)
    memo={} # or memo = [[[-1]*2 for _ in range(k)] for _ in range(n+1)]
    def f(i,rem,taken):
        if i==n:
            return rem==0 and taken 
        if (i,rem,taken) in memo:
            return memo[(i,rem,taken)]
        
        take=f(i+1,(rem+arr[i])%k,True)
        notTake=f(i+1,rem,taken)
        memo[(i,rem,taken)]=take or notTake 

        return memo[(i,rem,taken)]
    
    return f(0,0,False)

# dp tabulation
def tabulation(arr,k):
    # rem can take from 0,1,......k-1
    # i can take 0 to n --> n+1 values
    # rem --> 0 to k-1, --> k values
    # taken --> 2 values
    # (n+1)*k*2
    n=len(arr)
    dp=[[[False]*2 for _ in range(k)] for _ in range(n+1)]
    # from recursion if i==n: return rem==0 and taken 
    for rem in range(k):
        dp[n][rem][0]=False
        dp[n][rem][1]=(rem==0)
    
    # fill table
    for i in range(n-1,-1,-1):
        for rem in range(k):
            for taken in range(2):
                notTake=dp[i+1][rem][taken]

                take=dp[i+1][(rem+arr[i])%k][1]

                dp[i][rem][taken]=take or notTake
    return dp[0][0][0]

# mostly above solution is not used 
# optimized code, is to use a set of possible remainders
def subsetDivisble(arr,k):
    possible=set()
    for num in arr:
        new=possible.copy()

        # subset containing only num 
        new.add(num%k)
        # append num to all previous subsets
        for rem in possible:
            new.add((rem+num)%k)
        
        possible=new 

        if 0 in possible:
            return True 
        
    return False

print(memoization(arr,k))
print(tabulation(arr,k))
print(subsetDivisble(arr,k))