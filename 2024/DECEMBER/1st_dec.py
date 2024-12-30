# Non Repeating Character
# return the first non repeating character in a string

s="geeksforgeeks"

def non_repeating(s):
    map={}
    for c in s:
        if c in map:
            map[c]+=1
        else:
            map[c]=1
    
    for k,v in map.items():
        if v==1:
            return k
        
    return -1

print(non_repeating(s))