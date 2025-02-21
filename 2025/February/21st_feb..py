# Parenthesis Checker

s="[{()}]"

def parenthesisChecker(s):
    st=[]
    for ch in s:
        if ch in ['{','[','(']:
            st.append(ch)
        else:
            if not st:
                return False
            if ch=='}' and st[-1]=='{':
                st.pop()
            elif ch==']' and st[-1]=='[':
                st.pop()
            elif ch==')' and st[-1]=='(':
                st.pop()
            else:
                return False
            
    return not st

print(parenthesisChecker(s))  # True