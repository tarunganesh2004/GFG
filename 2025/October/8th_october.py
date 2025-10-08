# Build Binary Tree From PreOrder and PostOrder Traversal

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    @property
    def left(self):
        raise NotImplementedError

    @left.setter
    def left(self, value):
        raise NotImplementedError


class Solution:
    def constructTree(self,pre,post):
        if not pre or not post:
            return None 
        
        root=Node(pre[0])
        if len(pre)==1:
            return root
        left_subtree_root=pre[1]
        left_subtree_size=post.index(left_subtree_root)+1
        
        left_preorder=pre[1:left_subtree_size+1]
        right_preorder=pre[left_subtree_size+1:]

        left_postorder=post[:left_subtree_size]
        right_postorder=post[left_subtree_size:-1]

        root.left=self.constructTree(left_preorder,left_postorder)
        root.right=self.constructTree(right_preorder,right_postorder) # type: ignore
        return root
    
def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.val, end=' ')
    printInorder(node.right)

pre=[1, 2, 4, 5, 3, 6, 7]
post=[4, 5, 2, 6, 7, 3, 1]
sol=Solution()
root=sol.constructTree(pre,post)
print("Inorder traversal of the constructed tree:")
printInorder(root)