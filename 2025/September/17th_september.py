# Decode String

s="3[b2[ca]]"

def decodeString(s):
    st=[]
    for c in s:
        if c!="]":
            st.append(c)
        else:
            substr=""
            while st and st[-1]!="[":
                substr=st.pop()+substr
            st.pop()
            k=""
            while st and st[-1].isdigit():
                k=st.pop()+k
            st.append(int(k)*substr)
    return "".join(st)

print(decodeString(s))