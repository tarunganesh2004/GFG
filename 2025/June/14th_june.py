# Symmetric Tree 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def buildTree(self,arr):
        if not arr or arr[0] == 'N':
            return None
        root= Node(arr[0])
        queue = [root]
        i = 1
        while i < len(arr):
            current = queue.pop(0)
            if arr[i] != 'N':
                current.left = Node(arr[i])
                queue.append(current.left)
            i += 1
            if i < len(arr) and arr[i] != 'N':
                current.right = Node(arr[i])
                queue.append(current.right)
            i += 1
        return root
    
class Solution:
    def isSymmetric(self, root: Node) -> bool:
        if not root:
            return True
        
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.data == right.data and 
                    isMirror(left.left, right.right) and 
                    isMirror(left.right, right.left))
        
        return isMirror(root.left, root.right)

arr=[1, 2, 2, 3, 4, 4, 3]
root = Node(0).buildTree(arr)
sol = Solution()
print(sol.isSymmetric(root))  # type: ignore # Output: True