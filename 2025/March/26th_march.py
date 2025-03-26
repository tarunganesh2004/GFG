# Word Break

s="ilike"
dict=["i","like","anime"]

# Recursion
def recur(s):
    if s=="":
        return True
    
    for i in range(1,len(s)+1):
        if s[:i] in dict and recur(s[i:]):
            return True
    
    return False

# using lru_cache
def memoi_recur(s):
    from functools import lru_cache
    @lru_cache(None)
    def recur(s):
        if s=="":
            return True
        
        for i in range(1,len(s)+1):
            if s[:i] in dict and recur(s[i:]):
                return True
        
        return False
    
    return recur(s)

# memoization
def memoization(s):
    memo={}
    def recurMemo(s):
        if s in memo:
            return memo[s]
        
        if s=="":
            return True
        
        for i in range(1,len(s)+1):
            if s[:i] in dict and recurMemo(s[i:]):
                memo[s]=True
                return True
        
        memo[s]=False
        return False
    
    return recurMemo(s)

print(recur(s))
print(memoi_recur(s))
print(memoization(s))