# Stickler Thief II

arr=[2,3,2] # houses are in circle. so first and last house cannot be robbed together

# recursion
def brute_force(arr):
    def recur(cur_idx,n):
        if cur_idx>=n:
            return 0
        
        # include current
        include=arr[cur_idx]+recur(cur_idx+2,n)
        # exclude current
        exclude=recur(cur_idx+1,n)
        return max(include,exclude)
    
    n=len(arr)
    # case 1 rob from house [0] to house [n-2](excluding last house)
    case1=recur(0,n-1)
    # case 2 rob from house [1] to house [n-1](excluding first house)
    case2=recur(1,n)

    return max(case1,case2)

# using lru_cache
def brute_force_memoi(arr):
    from functools import lru_cache
    arr=tuple(arr)

    @lru_cache(None)
    def recur(cur_idx,n):
        if cur_idx>=n:
            return 0
        
        # include current
        include=arr[cur_idx]+recur(cur_idx+2,n)
        # exclude current
        exclude=recur(cur_idx+1,n)
        return max(include,exclude)
    
    n=len(arr)
    # case 1 rob from house [0] to house [n-2](excluding last house)
    case1=recur(0,n-1)
    # case 2 rob from house [1] to house [n-1](excluding first house)
    case2=recur(1,n)

    return max(case1,case2)

# memoization
def memoization(arr):
    memo={}
    def recurMemo(cur_idx,n,memo):
        if cur_idx>=n:
            return 0
        
        if cur_idx in memo:
            return memo[cur_idx]
        
        # include current
        include=arr[cur_idx]+recurMemo(cur_idx+2,n,memo)
        # exclude current
        exclude=recurMemo(cur_idx+1,n,memo)

        memo[cur_idx]=max(include,exclude)
        return memo[cur_idx]
    
    n=len(arr)
    # case 1 rob from house [0] to house [n-2](excluding last house)
    case1=recurMemo(0,n-1,memo)
    # case 2 rob from house [1] to house [n-1](excluding first house)
    case2=recurMemo(1,n,memo)

    return max(case1,case2)

print(brute_force(arr))
print(brute_force_memoi(arr)) # 3
print(memoization(arr)) # 3