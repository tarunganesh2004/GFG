# Min Add To Make Parentheses Valid

s="(()("

def minParentheses(s):
    left=0
    right=0
    for i in s:
        if i=='(':
            left+=1
        else:
            if left>0:
                left-=1
            else:
                right+=1
    return left+right

print(minParentheses(s))