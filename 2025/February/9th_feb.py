# Maximum Path sum from any node

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def buildTree(self,arr):
        if not arr or arr[0] == 'N':
            return None
        q=[]
        root=TreeNode(arr[0])
        i=1
        q.append(root)
        while i<len(arr) and q:
            node=q.pop(0)
            if i<len(arr) and arr[i]!='N':
                node.left=TreeNode(arr[i])
                q.append(node.left)
            i+=1
            if i>=len(arr):
                break
            if i<len(arr) and arr[i]!='N':
                node.right=TreeNode(arr[i])
                q.append(node.right)
            i+=1
        return root
    
class Solution:
    def maxPathSum(self,root):
        if not root:
            return 0
        res=[float('-inf')]
        def dfs(node):
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            res[0]=max(res[0],node.data+left+right)
            return max(0,node.data+max(left,right))
        dfs(root)
        return res[0]
    
arr=[10,2,10,20,1,"N",-25,"N","N","N","N",3,4]
root=TreeNode(arr)
root=root.buildTree(arr)
sol=Solution()
print(sol.maxPathSum(root)) # 42