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

print(longestStrChain(words)) # 4