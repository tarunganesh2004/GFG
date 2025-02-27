# # Get Min from Stack

# Given q queries, You task is to implement the following four functions for a stack:

# push(x) – Insert an integer x onto the stack.
# pop() – Remove the top element from the stack.
# peek() - Return the top element from the stack. If the stack is empty, return -1.
# getMin() – Retrieve the minimum element from the stack in O(1) time. If the stack is empty, return -1.
# Each query can be one of the following:

# 1 x : Push x onto the stack.
# 2 : Pop the top element from the stack.
# 3: Return the top element from the stack. If the stack is empty, return -1.
# 4: Return the minimum element from the stack.

class Solution:
    def __init__(self):
        self.st=[]
        self.minSt=[]

    def push(self,x):
        self.st.append(x)
        if not self.minSt or x<=self.minSt[-1]:
            self.minSt.append(x)

    def pop(self):
        if self.st:
            if self.st[-1]==self.minSt[-1]:
                self.minSt.pop()
            self.st.pop()

    def peek(self):
        return self.st[-1] if self.st else -1
    
    def getMin(self):
        return self.minSt[-1] if self.minSt else -1
    

s=Solution()
queries=[[1,2],[1,3],[3],[2],[4],[1,1],[4]]
for query in queries:
    if query[0]==1:
        s.push(query[1])
    elif query[0]==2:
        s.pop()
    elif query[0]==3:
        print(s.peek())
    else:
        print(s.getMin())

        