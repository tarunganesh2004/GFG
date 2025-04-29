# Maximum Sum of Non adjacent Nodes

from collections import deque


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def buildTree(s):
    if len(s)==0 or s[0]=="N":
        return None
    
    ip=list(map(str,s.split()))
    root=Node(int(ip[0]))
    q=deque()
    size=0
    q.append(root)
    size+=1
    i=1
    while size>0 and i<len(ip):
        curNode=q[0]
        q.popleft()
        size-=1
        curVal=ip[i]
        if curVal!="N":
            curNode.left=Node(int(curVal))
            q.append(curNode.left)
            size+=1
        i+=1
        if i>=len(ip):
            break
        curVal=ip[i]
        if curVal!="N":
            curNode.right=Node(int(curVal))
            q.append(curNode.right)
            size+=1
        i+=1
    return root

class Solution:
    def maxSum(self,root):
        def dfs(root):
            if not root:
                return (0, 0)
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            # Include current node's value
            include = root.val + left[1] + right[1]
            
            # Exclude current node's value
            exclude = max(left) + max(right)
            
            return (include, exclude)
        
        return max(dfs(root))
    
s="11 1 2"
root=buildTree(s)
sol=Solution()
print(sol.maxSum(root))  