# Remove the Balls

color=[2,3,5]
radius=[3,3,5]

def findLength(color,radius):
    stack=[]
    for i,j in zip(color,radius):
        if stack and stack[-1]==(i,j):
            stack.pop()
        else:
            stack.append((i,j))
    return len(stack)

print(findLength(color, radius))  # Output: 3