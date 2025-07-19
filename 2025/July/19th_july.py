# Count Unique Vowel Strings

s="aeiou"

def vowel_count(s):
    def fact(n):
        res=1
        for i in range(1,n+1):
            res *= i
        return res
    freq={}
    vowels='aeiou'

    for c in s:
        if c in vowels:
            freq[c]=freq.get(c,0)+1
    
    if not freq:
        return 0
    choices=1 
    for count in freq.values():
        choices*=count
    
    dist=len(freq)
    res=choices*fact(dist)
    return res

print(vowel_count(s))