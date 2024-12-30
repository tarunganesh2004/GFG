# minimum repeat to make substring

s1="ww"
s2="wwww" 

def isSubstring(s1,s2):
    return s2 in s1
def minRepeat(s1,s2):
    if len(s1)>len(s2):
        if s1.__contains__(s2):
            return 0
        else:
            return -1
        
    repeated=s1 # repeated once
    rep=1

    while len(repeated)<len(s1)+len(s2):
        if isSubstring(repeated,s2):
            return rep
        
        repeated+=s1 # adds another repeat of s1
        rep+=1

    if isSubstring(repeated,s2):
        return rep
    
    return -1
        
    
print(minRepeat(s1,s2))
