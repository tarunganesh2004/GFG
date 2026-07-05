# Max Gap between two same

s="socks"

def maxCharGapBrute(s):
    ans=0
    for ch in set(s):
        first=s.index(ch)
        last=s.rindex(ch)

        gap=last-first-1
        ans=max(ans,gap)
    return ans

def maxCharGap(s):
    # in one pass 
    first={}
    ans=-1
    for i,ch in enumerate(s):
        if ch not in first:
            first[ch]=i
        else:
            gap=i-first[ch]-1
            ans=max(ans,gap)
    return ans

print(maxCharGap(s))