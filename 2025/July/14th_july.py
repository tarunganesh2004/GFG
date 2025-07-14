# Cutting Binary String 

s="101101101"

# recursion
def bruteForce(s):
    def isPowerOf5(str):
        if str[0]=="0":
            return False
        num = int(str, 2)
        while num>1:
            if num%5!=0:
                return False
            num //= 5
        return True
    
    def recur(i,s):
        if i==len(s):
            return 0
        min_cuts=float('inf')
        for j in range(i+1, len(s)+1):
            if isPowerOf5(s[i:j]):
                res=recur(j,s)
                if res!=-1:
                    min_cuts = min(min_cuts, 1 + res)
        return min_cuts if min_cuts != float('inf') else -1
    
    return recur(0, s)

# using lru_cache
def memoized(s):
    from functools import lru_cache
    def isPowerOf5(str):
        if str[0] == "0":
            return False
        num = int(str, 2)
        while num > 1:
            if num % 5 != 0:
                return False
            num //= 5
        return True
    @lru_cache(None)
    def recur(i):
        if i == len(s):
            return 0
        min_cuts = float('inf')
        for j in range(i + 1, len(s) + 1):
            if isPowerOf5(s[i:j]):
                res = recur(j)
                if res != -1:
                    min_cuts = min(min_cuts, 1 + res)
        return min_cuts if min_cuts != float('inf') else -1
    return recur(0)

# DP
def dp(s):
    def isPowerOf5(str):
        if str[0] == "0":
            return False
        num = int(str, 2)
        while num > 1:
            if num % 5 != 0:
                return False
            num //= 5
        return True
    
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0]=0 # empty string requires 0 cuts
    for i in range(1,n+1): # dp[i] for prefix s[0:i]
        for j in range(i):
            if isPowerOf5(s[j:i]):
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[n] if dp[n] != float('inf') else -1

print(bruteForce(s))  # Output: 3
print(memoized(s))  # Output: 3
print(dp(s))  # Output: 3