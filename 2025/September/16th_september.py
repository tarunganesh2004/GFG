# Postfix Evaluation

import math


arr=["2", "3","1", "*",  "+","9","-"]

def evaluatePostFix(arr):
    stack=[]
    for token in arr:
        if token not in "+-*/^":
            stack.append(int(token))
        else:
            b=stack.pop()
            a=stack.pop()
            if token=="+":
                stack.append(a+b)
            elif token=="-":
                stack.append(a-b)
            elif token=="*":
                stack.append(a*b)
            elif token=="/":
                stack.append(a//b)
            elif token=="^":
                stack.append(int(math.pow(a,b)))
    return stack[0]

print(evaluatePostFix(arr))