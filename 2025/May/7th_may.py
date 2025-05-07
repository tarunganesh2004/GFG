# Root to leaf paths

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class BinaryTree:
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
            if i >= len(arr):
                break
            if i < len(arr) and arr[i] is not None:
                current.right = Node(arr[i]) # type: ignore
                queue.append(current.right) # type: ignore
            i += 1
        return self.root
    

class Solution:
    def Paths(self,root):
        paths=[]
        self.dfs(root,[],paths)
        return paths
    
    def dfs(self,root,path,paths):
        if root is None:
            return 
        path.append(root.data)
        if root.left is None and root.right is None:
            paths.append(list(path))

        self.dfs(root.left,path,paths) # left child
        self.dfs(root.right,path,paths) # right child

        # remove the current node from path to backtrack
        path.pop()
    


arr=[1,2,3,4,5,None,None]
tree = BinaryTree()
tree.buildTree(arr)
sol = Solution()
print(sol.Paths(tree.root)) # Output: [[1, 2, 4], [1, 3]]