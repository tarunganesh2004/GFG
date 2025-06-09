# BST With Dead End

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

    def buildTree(self,arr):
        if not arr or arr[0]== 'N':
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
    def isDeadEnd(self,root):
        def check(n,left=0,right=float('inf')):
            if not n.left and not n.right:
                return n.data-1==left and n.data+1==right
            
            if n.left and check(n.left,left,n.data):
                return True
            if n.right and check(n.right,n.data,right):
                return True
            return False
        
        return check(root)
    
arr=[8,5,9,2,7,"N","N",1]
root = Node(0).buildTree(arr)
sol = Solution()
print(sol.isDeadEnd(root))  # Output: True, as there is a dead end at node 1