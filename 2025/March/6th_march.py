# Longest Common Subsequence

s1="ABCDGH"
s2="AEDFHR"

# brute force recursive
def lcs_recursive(s1,s2):
    if not s1 or not s2:
        return 0
    if s1[0]==s2[0]:
        return 1+lcs_recursive(s1[1:],s2[1:])
    return max(lcs_recursive(s1[1:],s2),lcs_recursive(s1,s2[1:]))

print(lcs_recursive(s1,s2)) # 3