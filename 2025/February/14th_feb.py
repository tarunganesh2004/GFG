# # Fixing two nodes of a BST

# Given the root of a Binary search tree(BST), where exactly two nodes were swapped by mistake. Your task is to fix (or correct) the BST by swapping them back. Do not change the structure of the tree.
# Note: It is guaranteed that the given input will form BST, except for 2 nodes that will be wrong. All changes must be reflected in the original linked list

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def buildTree(self, arr):
        if not arr or arr[0] == 'N':
            return None
        q = []
        root = Node(arr[0])
        i = 1
        q.append(root)
        while i < len(arr) and q:
            node = q.pop(0)
            if i < len(arr) and arr[i] != 'N':
                node.left = Node(arr[i])
                q.append(node.left)
            i += 1
            if i >= len(arr):
                break
            if i < len(arr) and arr[i] != 'N':
                node.right = Node(arr[i])
                q.append(node.right)
            i += 1
        return root
    
    def correctBST(self,root):
        # using stack
        c,stack=[],[]
        while root:
            stack.append(root)
            root=root.left
        while stack:
            cur=stack.pop()
            c.append(cur)
            cur=cur.right
            while cur:
                stack.append(cur)
                cur=cur.left
        
        i=0
        while i<len(c)-1:
            if c[i].data>c[i+1].data:
                break
            i+=1

        j=len(c)-1
        while j>0:
            if c[j].data<c[j-1].data:
                break
            j-=1

        c[i].data,c[j].data=c[j].data,c[i].data

        return root
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)

            

arr=[10,5,8,2,20]
tree=Node(0)
root=tree.buildTree(arr)
tree.inorder(root)
tree.correctBST(root)
print()
tree.inorder(root)