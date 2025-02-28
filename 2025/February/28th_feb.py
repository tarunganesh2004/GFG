# Evaluation of postfix expression
# import math
arr=['2','3','1','*','+','9','-']

def evaluatePostfix(arr):
    st=[]
    # for i in arr:
    #     if i.lstrip('-').isdigit():
    #         st.append(int(i))
    #     else:
    #         b=st.pop()
    #         a=st.pop()
    #         if i=='+':
    #             st.append(a+b)
    #         elif i=='-':
    #             st.append(a-b)
    #         elif i=='*':
    #             st.append(a*b)
    #         elif i=='/':
    #             st.append(math.trunc(a/b))
    # return st[-1]
    for i in arr:
        if i in "+-*/":
            b=st.pop()
            a=st.pop()
            if i=='+':
                st.append(a+b)
            elif i=='-':
                st.append(a-b)
            elif i=='*':
                st.append(a*b)
            elif i=='/':
                st.append(int(a/b))
        else:
            st.append(int(i))
    return st.pop()

arr1=['-8','3','/']
print(evaluatePostfix(arr1)) # -2
print(evaluatePostfix(arr)) # -4