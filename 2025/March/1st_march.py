# Decode String 

s="3[b2[ca]]"

def decodeString(s):
    st=[]
    for ch in s:
        if ch!=']':
            st.append(ch)
        else:
            temp_str=""
            while st[-1]!='[':
                temp_str=st.pop()+temp_str
            st.pop()
            num=""
            while st and st[-1].isdigit():
                num=st.pop()+num
            temp_str=int(num)*temp_str
            st.append(temp_str)
    return "".join(st)

print(decodeString(s))