# Min chars to Add for Palindrome

s="abc"

def computeLPSArray(s):
    n=len(s)
    lps=[0]*n

    lps[0]=0
    lps_len=0

    i=1
    while i<n:
        if s[i]==s[lps_len]:
            lps_len+=1
            lps[i]=lps_len
            i+=1
        else:
            if lps_len!=0:
                lps_len=lps[lps_len-1]
            else:
                lps[i]=0
                i+=1
    return lps

def minChar(s):
    n=len(s)
    rev=s[::-1]
    s=s+"$"+rev
    lps=computeLPSArray(s)
    return n-lps[-1]

print(minChar(s))