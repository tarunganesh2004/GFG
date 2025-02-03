# Height of Binary Tree 
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
    
    def height_of_binary_tree(self,root):
        if not root:
            return -1
        else:
            left_height=self.height_of_binary_tree(root.left)
            right_height=self.height_of_binary_tree(root.right)
            return max(left_height,right_height)+1
    
arr=[12,8,18,5,11]
root=TreeNode(None)
root=root.build_tree(arr)
print(root.height_of_binary_tree(root)) # type: ignore # 3