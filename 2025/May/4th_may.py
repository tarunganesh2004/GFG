# Smallest Distinct Window



s="aabcbcdbca"

def smallest_distinct_window(s):
    from collections import defaultdict
    unique_chars = set(s)
    required=len(unique_chars)
    freq=defaultdict(int)

    left=0
    min_len=float('inf')
    min_window=""
    count=0 # count of unique characters in current window
    for right in range(len(s)):
        freq[s[right]]+=1
        if freq[s[right]]==1:
            count+=1
        while count==required:
            if right-left+1<min_len:
                min_len=right-left+1
                min_window=s[left:right+1]
            freq[s[left]]-=1
            if freq[s[left]]==0:
                count-=1
            left+=1
    return min_len, min_window 

print(smallest_distinct_window(s)) 