# 0-1 Knapsack Problem

cap=4
wt=[4,5,1]
val=[1,2,3] # profit

# recursion
def recursion(cap,wt,val):
    def knap(i,cap,wt,val):
        if i<0 or cap==0:
            return 0
        if wt[i]>cap:
            return knap(i-1,cap,wt,val) # skip
        else:
            return max(val[i]+knap(i-1,cap-wt[i],wt,val),knap(i-1,cap,wt,val)) # include or skip
    return knap(len(wt)-1,cap,wt,val)

# memoization
def memoization(cap,wt,val):
    def knap(i,cap,wt,val,memo):
        if i<0 or cap==0:
            return 0
        if memo[i][cap]!=-1:
            return memo[i][cap]
        if wt[i]>cap:
            memo[i][cap]=knap(i-1,cap,wt,val,memo)
            return memo[i][cap]
        else:
            memo[i][cap]=max(val[i]+knap(i-1,cap-wt[i],wt,val,memo),knap(i-1,cap,wt,val,memo))
            return memo[i][cap]
    n=len(wt)
    memo=[[-1]*(cap+1) for _ in range(n)]
    return knap(n-1,cap,wt,val,memo)

print(recursion(cap,wt,val)) # 3
print(memoization(cap,wt,val)) # 3