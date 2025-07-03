# Longest Substring with K Uniques

s="aabacbebebe"
k=3

def longestSubstringWithKUnique(s, k):
    from collections import defaultdict
    n = len(s)
    left = 0
    max_len = -1
    count = defaultdict(int)
    for right in range(n):
        count[s[right]]+=1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        if len(count)==k:
            max_len = max(max_len, right - left + 1)
    return max_len

print(longestSubstringWithKUnique(s, k))