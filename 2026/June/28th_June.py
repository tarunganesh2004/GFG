# k Times appearing adjacent two 1's

n=3
k=2
from functools import lru_cache
MOD=10**9+7
# bruteforce
def bruteForce(n,k):
    # maintain, cnt,current idx, and previous bit as state

    #  num of ways to fill positions from i onwards, currently we have cnt adjacent '11' pairs and the previous bit is prev
    # f(i,cnt,prev)
    # ans=f(1,0,0)+f(1,0,1)
    # to convert this to memoization 
    @lru_cache(None)
    def dfs(i,cnt,prev): 
        if i==n:
            return 1 if cnt==k else 0 
        
        ans=0

        # put 0
        ans+=dfs(i+1,cnt,0)

        # put 1 
        if prev==1:
            ans+=dfs(i+1,cnt+1,1)
        else:
            # if prev is 0, then '11' doesnt form so no need to increment count
            ans+=dfs(i+1,cnt,1)
        
        return ans%MOD
    
    return (dfs(1,0,0)+dfs(1,0,1))%MOD

# memoization
def memoization(n,k):
    # states -- i,cnt,prev
    # i--> 0 to n --> size n+1
    # cnt --> we need exactly k pairs, so maximum useful value,0 to k, if it exceeds k,we can stop so size k+1
    # prev can only be 0 or 1, so size 2
    dp=[[[-1]*2 for _ in range(k+1)] for _ in range(n+1)]

    def dfs(i,cnt,prev):
        if cnt>k:
            return 0

        if i==n:
            return 1 if cnt==k else 0

        if dp[i][cnt][prev]!=-1:
            return dp[i][cnt][prev]

        ans=0

        # put 0
        ans+=dfs(i+1,cnt,0)

        # put 1
        if prev==1:
            ans+=dfs(i+1,cnt+1,1)
        else:
            ans+=dfs(i+1,cnt,1)

        dp[i][cnt][prev]=ans

        return dp[i][cnt][prev]

    return (dfs(1, 0, 0) + dfs(1, 0, 1)) % MOD


# now dp
def dp(n,k):
    # states -- i,cnt,prev
    # i--> 0 to n --> size n+1
    # cnt --> we need exactly k pairs, so maximum useful value,0 to k, if it exceeds k,we can stop so size k+1
    # prev can only be 0 or 1, so size 2
    # so the state is dp[i][cnt][prev]
    # how many ways i can fill the remaining positions
    # [0 .... i-1] → already decided
    # [i .... n-1] → still need to decide

    # put 0--> dp[i][cnt][prev]+=dp[i+1][cnt][0]
    # if prev==1 --> dp[i][cnt][1]+=dp[i+1][cnt+1][1], else dp[i][cnt][0]+=dp[i+1][cnt][1]
    dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)] # here we fill with 0 because initially 0 ways 

    # base row 
    dp[n][k][0]=1
    dp[n][k][1]=1

    for i in range(n-1,-1,-1):
        for cnt in range(k,-1,-1):

            # prev=0
            dp[i][cnt][0]=(dp[i+1][cnt][0]+dp[i+1][cnt][1])%MOD 

            # prev=1
            dp[i][cnt][1]=dp[i+1][cnt][0]
            if cnt<k:
                dp[i][cnt][1]+=dp[i+1][cnt+1][1]

            dp[i][cnt][1]%=MOD 

    return (dp[1][0][0]+dp[1][0][1])%MOD


print(bruteForce(n,k))
print(dp(n,k))
