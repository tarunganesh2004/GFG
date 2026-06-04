s="11000010001"

def maxSubstring(s):
    if not s:
        return 0
    if '0' not in s:
        return -1
    cur=0
    ans=float('-inf')

    for ch in s:
        val=1 if ch=='0' else -1

        cur+=val

        ans=max(cur,ans)
        if cur<0:
            cur=0
    return ans 

print(maxSubstring(s))