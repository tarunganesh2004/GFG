# Min Cost Climbing Stairs

cost=[10,15,20] # ways are from 10 to 20(cost=10+20=30) or start at 15 move 2 steps to goal(cost=15)

# recursion
def recursion(cost):
    def min_cost(i,cost):
        if i<0:
            return 0
        if i==0 or i==1:
            return cost[i]
        
        return cost[i]+min(min_cost(i-1,cost),min_cost(i-2,cost))
    return min(min_cost(len(cost)-1,cost),min_cost(len(cost)-2,cost))

# memoization
def memoi(cost):
    def min_cost(i,cost,memo):
        if i<0:
            return 0
        if i==0 or i==1:
            return cost[i]
        if memo[i]!=-1:
            return memo[i]
        
        memo[i]=cost[i]+min(min_cost(i-1,cost,memo),min_cost(i-2,cost,memo))
        return memo[i]
    n=len(cost)
    memo=[-1]*n
    return min(min_cost(len(cost)-1,cost,memo),min_cost(len(cost)-2,cost,memo))

print(recursion(cost))
print(memoi(cost)) # 15