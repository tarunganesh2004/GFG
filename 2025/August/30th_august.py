# The Celebrity Problem

mat=[[1,1,0],[0,1,0],[0,1,1]]

def celebrity(arr):
    stack=[]
    for i in range(len(arr)):
        # append all people
        stack.append(i)

    while len(stack)>=2:
        a=stack.pop()
        b=stack.pop()
        if arr[a][b]==1:
            stack.append(b)
        else:
            stack.append(a)

    celeb=stack.pop()
    for i in range(len(arr)):
        if i!=celeb and (arr[celeb][i]==1 or arr[i][celeb]==0):
            return -1
    return celeb

print(celebrity(mat))