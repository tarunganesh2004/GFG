# Tree Boundary Traversal
# left boundary,leaf nodes, reverse right boundary

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    @staticmethod
    def build_tree(arr):
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
    
class Solution:
    # left boundary(excluding leaf nodes)
    def left_boundary(self,root):
        if not root or (not root.left and not root.right):
            return []
        
        # if left child is present go left, else go right
        left=[]
        if root.left:
            left= [root.data]+self.left_boundary(root.left)
        else:
            left= [root.data]+self.left_boundary(root.right)
        return left
        

    # right boundary(excluding leaf nodes)
    def right_boundary(self,root):
        if not root or (not root.left and not root.right):
            return []
        
        right=[]
        # if right child is present go right, else go left
        if root.right:
            right= self.right_boundary(root.right)+[root.data]
        else:
            right= self.right_boundary(root.left)+[root.data]
        return right
    
    # leaf nodes
    def leaf_nodes(self,root):
        if not root:
            return []
        if not root.left and not root.right: # leaf node
            return [root.data]
        return self.leaf_nodes(root.left)+self.leaf_nodes(root.right)
    
    def boundary_traversal(self,root): # TC O(H) for left boundary, O(N) for leaf nodes, O(H) for right boundary total O(N)
        if not root:
            return []
        
        # for single node
        if not root.left and not root.right:
            return [root.data]
        

        left=self.left_boundary(root.left) # left boundary(excluding leaf nodes and root)
        leaf=self.leaf_nodes(root) # leaf nodes
        right=self.right_boundary(root.right) # right boundary(excluding leaf nodes and root)
        return [root.data]+left+leaf+right
    

arr=[1,2,3,4,5,6,7,"N","N",8,9,"N","N","N","N"]
root=TreeNode.build_tree(arr)
sol=Solution()
print(sol.boundary_traversal(root)) # type: ignore 