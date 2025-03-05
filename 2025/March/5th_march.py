# Longest String Chain

words=["ba","b","a","bca","bda","bdca"]

def longestStrChain(words):
    from collections import defaultdict
    words.sort(key=len)
    dp=defaultdict(int)
    for word in words:
        for i in range(len(word)):
            dp[word]=max(dp[word],dp[word[:i]+word[i+1:]]+1)
    return max(dp.values())

# optimized
def optimized(words):
    from collections import defaultdict
    s=set(words)
    ws=defaultdict(set)

    for w in words:
        for i in range(len(w)):
            e=w[:i]+w[i+1:]
            if e in s:
                ws[e].add(w)
    
    words.sort(key=len)
    cache=defaultdict(int)

    def dfs(w):
        if w in cache:
            return cache[w]
        
        r=1
        for c in ws[w]:
            r=max(r,dfs(c)+1)
        cache[w]=r
        return r
    
    res=0
    for w in words:
        res=max(res,dfs(w))
    return res

print(longestStrChain(words)) # 4
print(optimized(words)) # 4