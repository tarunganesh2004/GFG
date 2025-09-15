# String stack

pat="geuaek"
tar="geek"

def stringStack(pat,tar):
    i=len(pat)-1
    j=len(tar)-1
    while i>=0 and j>=0:
        if pat[i]==tar[j]:
            i-=1
            j-=1
        else:
            i-=2
    return j<0

print(stringStack(pat,tar))