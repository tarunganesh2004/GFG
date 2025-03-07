# Longest Palindromic Subsequence

s="bbabcbcab"

# recursive

def lps_recursive(s,i,j): # O(2^n) 
    if i==j: # if there is only one character
        return 1
    if i>j:
        return 0
    
    if s[i]==s[j]:
        return 2+lps_recursive(s,i+1,j-1) # 2 characters are same, so 2 is added and the remaining string is checked
    else:
        return max(lps_recursive(s,i+1,j),lps_recursive(s,i,j-1))
    

    
print(lps_recursive(s,0,len(s)-1)) # 7