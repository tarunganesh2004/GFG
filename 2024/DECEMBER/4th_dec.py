# Strings Rotations of each other

s1="abcd"
s2="cdab"

def areRotations(s1,s2):
    temp = s1+s1
    if s2 in temp:
        return True
    else:
        return False

print(areRotations(s1,s2))