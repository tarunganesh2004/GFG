# Post Order Traversal

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def buildTree(self,arr):
        if arr[0]==-1 or len(arr)==0:
            return None
        root=Node(arr[0])
        queue=[root]
        i=1
        while queue and i<len(arr):
            current=queue.pop(0)
            if arr[i]!=-1:
                current.left=Node(arr[i]) # type: ignore
                queue.append(current.left) # type: ignore
            i+=1
            if i>len(arr):
                break
            if i<len(arr) and arr[i]!=-1:
                current.right=Node(arr[i]) # type: ignore
                queue.append(current.right) # type: ignore
            i+=1

        return root
    
    def inOrder(self,root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.val,end=' ')
        self.inOrder(root.right)

class Solution:
    def postOrder(self,root):
        res=[]
        def helper(node):
            if node is None:
                return
            helper(node.left)
            helper(node.right)
            res.append(node.val)
        helper(root)
        return res
    
arr=[1,2,3,4,5,-1,6,-1,-1,-1,-1,-1,7]
bt=BinaryTree()
root=bt.buildTree(arr)
bt.inOrder(root)
print()
sol=Solution()
print(sol.postOrder(root))
