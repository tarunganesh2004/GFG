# Is Binary ree Heap

from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def buildTree(s):
    if len(s)==0 or s[0]=="N":
        return None
    ip = list(map(str, s.split()))
    root = Node(int(ip[0]))
    size=0
    q=deque()
    q.append(root)
    size+=1
    i=1
    while size>0 and i<len(ip):
        currNode=q.popleft()
        size-=1
        currVal=ip[i]
        if currVal!="N":
            currNode.left=Node(int(currVal))
            q.append(currNode.left)
            size+=1
        i+=1
        if i>=len(ip):
            break
        currVal=ip[i]
        if currVal!="N":
            currNode.right=Node(int(currVal))
            q.append(currNode.right)
            size+=1
        i+=1
    return root
class Solution:
    def isHeap(self,root):
        # using level order traversal
        if not root:
            return True
        q=deque()
        q.append(root)
        end=False
        while q:
            cur=q.popleft()
            if cur.left:
                if end:
                    return False
                if cur.val<cur.left.val:
                    return False
                q.append(cur.left)
            else:
                end=True
            if cur.right:
                if end:
                    return False
                if cur.val<cur.right.val:
                    return False
                q.append(cur.right)
            else:
                end=True
        return True
    

arr="10 9 8 7 6 N N N N 5 4 N N N N"
root=buildTree(arr)
sol=Solution()
print(sol.isHeap(root)) 