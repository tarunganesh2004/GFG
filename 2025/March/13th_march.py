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

print(recursion(cap,wt,val)) # 3