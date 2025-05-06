# Left View of Binary Tree

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root=None

    def buildTree(self,arr):
        if not arr:
            return None
        self.root = Node(arr[0])
        queue = [self.root]
        i = 1
        while queue and i < len(arr):
            current = queue.pop(0)
            if arr[i] is not None:
                current.left = Node(arr[i]) # type: ignore
                queue.append(current.left) # type: ignore
            i += 1
            if i>len(arr):
                break
            if i < len(arr) and arr[i] is not None:
                current.right = Node(arr[i]) # type: ignore
                queue.append(current.right) # type: ignore
            i += 1

        return self.root
    
    def leftView(self,root):
        return self.dfs(root,0,[])
    
    def dfs(self,root,level,view):
        if root is None:
            return
        if level==len(view):
            view.append(root.val)
        self.dfs(root.left,level+1,view)
        self.dfs(root.right,level+1,view)
        return view
    
arr=[1,2,3,4,5,None,6,7,None,None,None,None,8]
tree = BinaryTree()
tree.buildTree(arr)
print(tree.leftView(tree.root)) # Output: [1, 2, 4, 7]