# Word Break

s="ilike"
dict=["i","like","anime"]

# Recursion
def recur(s):
    if s=="":
        return True
    
    for i in range(1,len(s)+1):
        if s[:i] in dict and recur(s[i:]):
            return True
    
    return False

print(recur(s))