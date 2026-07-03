# Ways to Increase LCS By one

s1="abab"
s2="abc"

"""
The bruteforce idea is inserting everycharacter and computing lcs, and checking

# the main intuition
is inserting a character,and checking prefix lcs, cur character and suffix lcs

suppose if we insert c at index 1 in s1
The matching is:

a | c | b
a | c | b

LCS:
left + inserted char + right
(best match on left)
+
(inserted character)
+
(best match on right)

ans=left_lcs+1+right_lcs
# left lcs
pref[i][j]=lcs of s1[:i] and s2[:j]
# right lcs
suff[i][j]=lcs of s1[i:] and s2[j:] --> this is lcs filled backwards
left=pref[i][j]
middle=1
right=suff[i][j+1] # here j+1 bcz we already used s2[j] so continue from next character
s2[j] has already been used by the inserted character so next matching s2[j+1]

now checking every inserted position, and 
for each psition try every character in s2
if left+middle+right=L+1 (here L is lcs for entire s1,s2)
then inserting s2[j] at position i works 

duplicate handling
if s2="aaa"
At one insertion position, all three 'a's may satisfy the formula.
But inserting 'a' at that position counts only once.
Therefore:
used = set()
for every insertion position.
"""

def waysToIncreaseLCSBy1(s1,s2):
    # prefix lcs table LCS[:i],LCS[:j]
    n1,n2=len(s1),len(s2)
    pref=[[0]*(n2+1) for _ in range(n1+1)]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if s1[i-1]==s2[j-1]:
                pref[i][j]=1+pref[i-1][j-1]
            else:
                pref[i][j]=max(pref[i-1][j],pref[i][j-1])
    # current lcs
    L=pref[n1][n2]

    # suffix table LCS[i:],LCS[j:]
    suff=[[0]*(n2+1) for _ in range(n1+1)]
    for i in range(n1-1,-1,-1):
        for j in range(n2-1,-1,-1):
            if s1[i]==s2[j]:
                suff[i][j]=1+suff[i+1][j+1]
            else:
                suff[i][j]=max(suff[i+1][j],suff[i][j+1])

    ans=0
    # try every inserted position
    for i in range(n1+1):
        used=set()

        # Try matching inserted character
        # with every position in s2
        for j in range(n2):
            ch=s2[j]
            if ch in used:
                continue
            
            left=pref[i][j]
            right=suff[i][j+1]

            if left+1+right==L+1:
                ans+=1
                used.add(ch)
    return ans 

print(waysToIncreaseLCSBy1(s1,s2))