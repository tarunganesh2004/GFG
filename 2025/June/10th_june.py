# Exactly one swap



s="geek"

def countStringsBrute(s): # O(n^2) time complexity
    set1=set()
    set1.add(s)
    n=len(s)
    for i in range(n):
        for j in range(i+1,n):
            if s[i] != s[j]:
                swapped = list(s)
                swapped[i], swapped[j] = swapped[j], swapped[i]
                k=''.join(swapped)
                if k not in set1:
                    set1.add(k)
    return len(set1)

# optimized solution
def optimized(s):
    n=len(s)
    sum=n*(n-1)//2
    freq=[0]*26
    for char in s:
        freq[ord(char)-ord('a')]+=1
    
    count=0
    has_duplicate=False
    for i in range(26):
        if freq[i]>1:
            count+=(freq[i]*(freq[i]-1))//2
            has_duplicate=True
    return sum-count+(1 if has_duplicate else 0)

print(countStringsBrute(s))  # Output: 6, as there are 6 unique strings after one swap
print(optimized(s))  # Output: 6, as there are 6 unique strings after one swap