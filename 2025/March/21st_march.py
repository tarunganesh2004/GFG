# Stickler Thief

arr=[6,5,5,7,4]

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
    
    return recur(0,len(arr))

print(brute_force(arr)) # 15