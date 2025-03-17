

arr=[3,34,4,12,5,2]
sum=9

# recursion
def bruteForce(arr,sum):
    def recur(cur_idx,cur_sum):
        if cur_sum==0:
            return True
        if cur_idx>=len(arr):
            return False
        # include next element
        if cur_sum-arr[cur_idx]>=0:
            if recur(cur_idx+1,cur_sum-arr[cur_idx]):
                return True
        # exclude next element
        if recur(cur_idx+1,cur_sum):
            return True
        return False
    return recur(0,sum)

# using lru_cache
def bruteForceMemoi(arr,sum):
    from functools import lru_cache
    arr = tuple(arr)

    @lru_cache(None)
    def helper(cur_idx,cur_sum):
        if cur_sum==0:
            return True
        if cur_idx>=len(arr):
            return False
        # include next element
        if cur_sum-arr[cur_idx]>=0:
            if helper(cur_idx+1,cur_sum-arr[cur_idx]):
                return True
        # exclude next element
        if helper(cur_idx+1,cur_sum):
            return True
        return False
    
    return helper(0,sum)

print(bruteForce(arr,sum)) # True
print(bruteForceMemoi(arr,sum)) # True