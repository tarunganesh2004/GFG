# Construct Tree From Inorder and PreOrder

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
    
    def buildTree(self,inorder,preorder):
        inorder_idx_map={value:idx for idx,value in enumerate(inorder)}
        preorder_idx=[0]

        def constructTree(start,end):
            if start>end:
                return None
            root_val=preorder[preorder_idx[0]]
            root=TreeNode(root_val)
            preorder_idx[0]+=1

            # find the root index in inorder
            root_idx=inorder_idx_map[root_val]

            # build left subtree
            root.left=constructTree(start,root_idx-1)
            # build right subtree
            root.right=constructTree(root_idx+1,end)

            return root
        
        return constructTree(0,len(inorder)-1)
    
    def postOrder(self,root):
        if not root:
            return []
        return self.postOrder(root.left)+self.postOrder(root.right)+[root.data]

inorder=[1,6,8,7]
preorder=[1,6,7,8]
root = TreeNode(preorder[0])
root=root.buildTree(inorder,preorder)
print(root.postOrder(root)) # type: ignore # [8, 7, 6, 1]