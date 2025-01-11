# Length of longest substring with distinct characters

s="abcabcbb"

# brute force O(n^3)
def bruteForce(s):
    def is_unique(s):
        return len(s)==len(set(s))
    n=len(s)
    res=0
    for i in range(n):
        for j in range(i+1,n+1):
            if is_unique(s[i:j]):
                res=max(res,j-i)
    return res

# Sliding window
def slidingWindow(s): # O(n) & O(n)
    n=len(s)
    char_set=set()
    max_len=0
    start=0
    for end in range(n):
        while s[end] in char_set:
            char_set.remove(s[start])
            start+=1
        char_set.add(s[end])
        max_len=max(max_len,end-start+1)
    return max_len

# optimized O(n)& O(1) using ascii array for fixed charset
def optimized(s):
    last_idx=[-1]*128
    n=len(s)
    max_len=0
    start=0

    for end in range(n):
        if last_idx[ord(s[end])]>=start:
            start=last_idx[ord(s[end])]+1
        last_idx[ord(s[end])]=end
        max_len=max(max_len,end-start+1)
    return max_len


print(bruteForce(s)) # 3
print(slidingWindow(s)) # 3
print(optimized(s)) # 3