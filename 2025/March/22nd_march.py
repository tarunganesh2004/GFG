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

print(brute_force(arr))