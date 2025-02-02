# Level Order Traversal

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
    
    def level_order_traversal(self,root):
        if not root:
            return []
        q=[]
        q.append(root)
        res=[]
        while q:
            n=len(q)
            tmp=[]
            for _ in range(n):
                node=q.pop(0)
                tmp.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(tmp)

        return res

arr=[1,3,2,'N','N',4,6,5]
root=TreeNode(None)
root=root.build_tree(arr)
print(root.level_order_traversal(root)) # type: ignore # [[1], [3, 2], [4, 6], [5]]