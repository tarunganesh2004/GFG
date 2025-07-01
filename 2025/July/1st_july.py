# Substrings of length k with k-1 distinct characters

s="aabc"
k=2

# brute force
def bruteForce(s,k):
    n=len(s)
    # generate all substrings of length k
    substrings = set()
    for i in range(n-k+1):
        substring = s[i:i+k]
        # check if it has k-1 distinct characters
        if len(set(substring)) == k-1:
            substrings.add(substring)
    return len(substrings)

# optimized
def optimized(s, k):
    n=len(s)
    i,j,cnt=0,0,0
    map=dict()
    while j<n:
        if s[j] in map:
            map[s[j]] += 1
        else:
            map[s[j]] = 1

        if j-i+1 < k:
            j += 1
        elif j-i+1 == k:
            if len(map) == k-1:
                cnt += 1
            
            # remove the leftmost character
            map[s[i]] -= 1
            if map[s[i]] == 0:
                del map[s[i]]
            i += 1
            j += 1
    return cnt


print(bruteForce(s,k))
print(optimized(s,k))