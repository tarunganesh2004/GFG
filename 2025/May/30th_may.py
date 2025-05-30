# Closest Neighbour in BST

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def buildTree(self, values):
        if not values:
            return None
        root = Node(values[0])
        queue = [root]
        i = 1
        while i < len(values):
            current = queue.pop(0)
            if values[i] is not None:
                current.left = Node(values[i])
                queue.append(current.left)
            i += 1
            if i>len(values):
                break
            if i < len(values) and values[i] is not None:
                current.right = Node(values[i])
                queue.append(current.right)
            i += 1
        return root
    
    def inorder(self,root):
        arr=[]
        
        def inorder_helper(root,arr):
            if root is None:
                return
            inorder_helper(root.left, arr)
            arr.append(root.data)
            inorder_helper(root.right, arr)
        return arr
    
def closest_neighbour(root,target):
    arr= root.inorder(root)
    # greatest element less than or equal to target
    closest = None
    for num in arr:
        if num <= target:
            if closest is None or num > closest:
                closest = num
    return closest

arr=[10,7,15,2,8,11,16]
k=14
root = Node(0).buildTree(arr)
print(closest_neighbour(root, k))  # Output: 11
