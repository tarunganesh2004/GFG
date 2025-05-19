# Predecessor and Successor

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def buildTree(self, arr):
        if not arr or arr[0]=="N":
            return None
        root = Node(arr[0])
        queue = [root]
        i = 1
        while queue and i < len(arr):
            currNode = queue.pop(0)
            if arr[i] != 'N':
                currNode.left = Node(arr[i])
                queue.append(currNode.left)
            i += 1
            if i >= len(arr):
                break
            if arr[i] != 'N':
                currNode.right = Node(arr[i])
                queue.append(currNode.right)
            i += 1
        return root

class Solution:
    def findPreSuc(self, root, key):
        def pred(root,key,ans):
            if root is None:
                return ans
            if root.data>=key:
                return pred(root.left,key,ans)
            elif root.data<key:
                ans=root
                return pred(root.right,key,ans)
            
        def succ(root,key,ans):
            if root is None:
                return ans
            if root.data<=key:
                return succ(root.right,key,ans)
            elif root.data>key:
                ans=root
                return succ(root.left,key,ans)
        
        return [pred(root,key,None),succ(root,key,None)]
    

root=[8,1,9,"N",4,"N",10,3,"N","N","N"]
key=8
n=Node(0)
root=n.buildTree(root)
s=Solution()
result=s.findPreSuc(root,key)
print(result)