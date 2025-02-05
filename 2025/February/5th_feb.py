# Mirror Tree 

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def build_tree(self,arr):
        if not arr or arr[0] == 'N':
            return None
        
        root = TreeNode(arr[0])
        i = 1
        q = []
        q.append(root)
        while i < len(arr) and q:
            node = q.pop(0)
            if arr[i] != 'N':
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i += 1
            if i>=len(arr):
                break
            if i < len(arr) and arr[i] != 'N':
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1

        return root
    
    # mirror of a tree is obtained by swapping the left and right children of each node
    def mirror(self,root):
        if not root:
            return None
        
        self.mirror(root.left)
        self.mirror(root.right)

        root.left,root.right=root.right,root.left
        return root
    
    def levelOrdr(self,root):
        if not root:
            return []
        
        q=[]
        q.append(root)
        res=[]
        while q:
            node=q.pop(0)
            res.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return res

arr=[1,2,3,'N','N',4]
root=TreeNode(arr[0])
root=root.build_tree(arr)

root.mirror(root) # type: ignore
print(root.levelOrdr(root)) # type: ignore