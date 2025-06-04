# Count substrings with k Distinct Characters

s="abc"
k=2

def countSubstringsWithKDistinct(s, k):
    n=len(s)
    char_count={}
    start_idx=0
    count=0
    for end_idx in range(n):
        char_count[s[end_idx]]=char_count.get(s[end_idx],0)+1
        while len(char_count)>k:
            first_char=s[start_idx]
            if char_count[first_char]==1:
                del char_count[first_char]
            else:
                char_count[first_char]-=1
            start_idx+=1
        count+= (end_idx - start_idx + 1)
    return count

def substringCount(s, k):
    return countSubstringsWithKDistinct(s, k)-countSubstringsWithKDistinct(s, k-1)

print(substringCount(s, k))  # Output: 2