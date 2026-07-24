# Longest Consecutive Path in Binary Tree

from collections import deque 
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.right=None 

class BinaryTree:
    def __init__(self):
        self.root=None 

    def buildTree(self,arr):
        if arr is None or len(arr)==0 or arr[0]=="N":
            return None 
        self.root=Node(arr[0])

        q=deque()
        q.append(self.root)
        i=1

        while q and i<len(arr):
            if i<len(arr) and arr[i]!="N":
                cur=q.popleft()
                cur.left=Node(arr[i])
                q.append(cur.left)
            i+=1
            if i>len(arr):
                break 
            if i<len(arr) and arr[i]!="N":
                cur.right=Node(arr[i])
                q.append(cur.right)
            i+=1
        return self.root 


class Solution:
    def longestConsecutive(self,root):
        if root is None:
            return -1
        
        def dfs(cur,parent,curLen,longestPath):
            if cur is None:
                return 
            if parent and cur.data==parent.data+1:
                curLen+=1
            else:
                curLen=1

            longestPath[0]=max(longestPath[0],curLen)

            dfs(cur.left,cur,curLen,longestPath)
            dfs(cur.right,cur,curLen,longestPath)
        
        longestPath=[0]
        dfs(root,None,0,longestPath)
        return -1 if longestPath[0]==1 else longestPath[0]

arr = [1, 2, 3, 3, 4, "N", "N", "N", "N", "N", 5]

tree = BinaryTree()
root = tree.buildTree(arr)

solution = Solution()
answer = solution.longestConsecutive(root)
print("Longest Consecutive Path Length:", answer)
