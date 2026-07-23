# Preorder Traversal

root=[1,4,"N",4,2]

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None 
        self.right=None 

class Solution:
    def preOrder(self,root):
        res=[]
        def dfs(cur):
            if cur is None:
                return 
            res.append(cur)
            dfs(cur.left) 
            dfs(cur.right)

        dfs(root)
        return res