# Matrix Chain Multiplication

arr=[2,1,3,4]

# brute force
def brute_force(arr):
    def recur(start,end):
        if start==end:
            return 0
        
        min_cost=float("inf")
        for k in range(start,end):
            left=recur(start,k)
            right=recur(k+1,end)
            cost=left+right+(arr[start-1]*arr[k]*arr[end])
            min_cost=min(min_cost,cost)
        
        return min_cost
    
    return recur(1,len(arr)-1)

print(brute_force(arr)) # 20