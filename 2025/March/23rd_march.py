# Total Decoding Messages
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

digits="123" 

# recursion
def brute_force(digits):

    def recur(cur_idx, n):
        print(f"Calling recur({cur_idx}, {n})")  # Debug step

        if cur_idx >= n:
            print(f"Reached end at index {cur_idx}. Returning 1.")
            return 1
        
        if digits[cur_idx] == "0":  # If the digit is 0, it can't be decoded
            print(f"Reached 0 at index {cur_idx}. Returning 0.")

        # Include current single digit
        print(f"Including {digits[cur_idx]} at index {cur_idx}")
        include = recur(cur_idx + 1, n)

        # Include two digits (if valid)
        include_2 = 0
        if cur_idx + 1 < n and int(digits[cur_idx : cur_idx + 2]) <= 26:
            print(f"Including {digits[cur_idx : cur_idx + 2]} at index {cur_idx}")
            include_2 = recur(cur_idx + 2, n)

        total_ways = include + include_2
        print(f"Returning from recur({cur_idx}, {n}): {total_ways}")
        return total_ways

    n = len(digits)
    return recur(0, n)

# using lru_cache
def memoi_brute_force(digits):
    from functools import lru_cache

    # digits=tuple(digits)
    n=len(digits)
    @lru_cache(None)
    def recur(cur_idx,n):
        if cur_idx>=n:
            return 1
        
        if digits[cur_idx]=="0": # if the digit is 0, it can't be decoded
            return 0
        
        # include cur digit(single)
        include=recur(cur_idx+1,n)

        # include cur digit and next digit
        include_2=0
        if cur_idx+1<n and int(digits[cur_idx:cur_idx+2])<=26:
            include_2=recur(cur_idx+2,n)

        return include+include_2
    
    return recur(0,n)

# memoization
def memoization(digits):
    def recurMemo(cur_idx,n,memo):
        if cur_idx>=n:
            return 1
        
        if cur_idx in memo:
            return memo[cur_idx]
        
        if digits[cur_idx]=="0": # if the digit is 0, it can't be decoded
            return 0
        
        # include current
        include=recurMemo(cur_idx+1,n,memo)
        # include current and next
        include_2=0
        if cur_idx+1<n and int(digits[cur_idx:cur_idx+2])<=26:
            include_2=recurMemo(cur_idx+2,n,memo)

        memo[cur_idx]=include+include_2
        return memo[cur_idx]
    
    n=len(digits)
    return recurMemo(0,n,{})

# dp
def dp(digits):
    n=len(digits)
    if n==0:
        return 0
    
    dp=[0]*(n+1)
    dp[n]=1 # base case

    for i in range(n-1,-1,-1):
        if digits[i]!="0":
            dp[i]=dp[i+1]
        
        if i+1<n and int(digits[i:i+2])<=26:
            dp[i]+=dp[i+2]

    return dp[0]


print(brute_force(digits)) # 3
print(memoi_brute_force(digits)) # 3
print(memoization(digits)) # 3
print(dp(digits)) # 3