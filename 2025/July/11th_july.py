# Trail Of Ones

n=3

def bruteForce(n): # O(2^n)
    def helper(pos,prev,hasConsec):
        if pos==n:
            return 1 if hasConsec else 0
        
        # add 0
        zero=helper(pos+1,0,hasConsec)
        # add 1
        one=helper(pos+1,1,hasConsec or (prev==1))
        return zero + one
    
    return helper(0,0,False)

# using lru_cache 
def memoized(n): # O(n)
    from functools import lru_cache
    @lru_cache(None)
    def helper(pos, prev, hasConsec):
        if pos == n:
            return 1 if hasConsec else 0
        
        # add 0
        zero = helper(pos + 1, 0, hasConsec)
        # add 1
        one = helper(pos + 1, 1, hasConsec or (prev == 1))
        return zero + one
    
    return helper(0, 0, False)

# DP
def dp(n):
    if n==1:
        return 0
    
    ending_with_0=[0]*(n+1)
    ending_with_1=[0]*(n+1)

    ending_with_0[1] = 1  # '0'
    ending_with_1[1] = 1  # '1'

    for i in range(2,n+1):
        ending_with_0[i]= ending_with_0[i-1] + ending_with_1[i-1]
        ending_with_1[i]=ending_with_0[i-1]

    good_strings= ending_with_0[n] + ending_with_1[n]
    total= 2**n  # Total binary strings of length n
    return total - good_strings  # Subtracting the good strings from total gives us the bad strings

print(bruteForce(n))  # Output: 3

print(memoized(n))  # Output: 3

print(dp(n))  # Output: 3