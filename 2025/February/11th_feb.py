# Check for BST

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def isBST(self,root,min,max):
        if not root:
            return True
        if root.data<=min or root.data>=max:
            return False
        return self.isBST(root.left,min,root.data) and self.isBST(root.right,root.data,max)
    
    def buildTree(self,arr):
        if not arr or arr[0] == 'N':
            return None
        q=[]
        root=Node(arr[0])
        i=1
        q.append(root)
        while i<len(arr) and q:
            node=q.pop(0)
            if i<len(arr) and arr[i]!='N':
                node.left=Node(arr[i])
                q.append(node.left)
            i+=1
            if i>=len(arr):
                break
            if i<len(arr) and arr[i]!='N':
                node.right=Node(arr[i])
                q.append(node.right)
            i+=1
        return root

arr = [2,1,3,"N","N","N",5]
root = Node(None)
root = root.buildTree(arr)
print(root.isBST(root,float("-inf"),float("inf"))) # type: ignore # True