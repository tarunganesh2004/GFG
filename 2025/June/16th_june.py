# Equalize the Towers


heights=[1,2,3]
cost=[10,100,1000]

def minCost(heights, cost):
    def costOfOperation(heights,cost,target):
        total_cost=0
        for h,c in zip(heights,cost):
            total_cost += abs(h - target) * c
        return total_cost
    
    low= min(heights)
    high= max(heights)
    min_cost = float('inf')
    while low<=high:
        mid1=low+(high-low)//3
        mid2=high-(high-low)//3

        cost1= costOfOperation(heights, cost, mid1)
        cost2= costOfOperation(heights, cost, mid2)

        min_cost= min(min_cost, cost1, cost2)

        if cost1== cost2:
            low= mid1+1
            high= mid2-1
        elif cost1 < cost2:
            high = mid2 - 1
        else:
            low = mid1 + 1
    return min_cost

result = minCost(heights, cost)
print(result)