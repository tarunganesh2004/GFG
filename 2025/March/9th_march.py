# Count Palindromic substrings(length>2)

s="abaab"
s1="abbaeae"

# brute force
def brute_force(s):
    count=0
    def isPalin(s):
        return s==s[::-1]
    
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if isPalin(s[i:j+1]):
                count+=1
    return count

# it can be solved in O(n^2) time complexity using dynamic programming, but space complexity will be O(n^2)

# better approach is expand around center
def countPalindromes(s):
    def expand(s,left,right):
        n=len(s)
        count=0
        while left>=0 and right<n and s[left]==s[right]:
            if right-left+1>=2: # length>2
                count+=1
            left-=1
            right+=1
        return count
    n=len(s)
    count=0
    for i in range(n):
        count+=expand(s,i,i) # odd length
        count+=expand(s,i,i+1)
    return count


print(brute_force(s1))
print(countPalindromes(s1)) # 4