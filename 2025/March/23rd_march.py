# Total Decoding Messages
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

digits="123" 

# recursion
def brute_force(digits):
    # If the string contains '0', it can't be decoded
    if "0" in digits:
        return 0

    def recur(cur_idx, n):
        print(f"Calling recur({cur_idx}, {n})")  # Debug step

        if cur_idx >= n:
            print(f"Reached end at index {cur_idx}. Returning 1.")
            return 1

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

print(brute_force(digits)) # 3
print(memoi_brute_force(digits)) # 3