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



print(brute_force(s1))