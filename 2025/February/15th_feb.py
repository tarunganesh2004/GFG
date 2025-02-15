# # Lowest Common Ancestor in a BST 

# Given a Binary Search Tree (with all values unique) and two nodes n1 and n2 (n1 != n2). You may assume that both nodes exist in the tree. Find the Lowest Common Ancestor (LCA) of the given two nodes in the BST.

# LCA between two nodes n1 and n2 is defined as the lowest node that has both n1 and n2 as descendants (where we allow a node to be a descendant of itself).

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

    def LCA(self,root,n1,n2):
        if root.data>n1 and root.data>n2:
            return self.LCA(root.left,n1,n2)
        if root.data<n1 and root.data<n2:
            return self.LCA(root.right,n1,n2)
        return root.data
    
    def otherApproach(self,root,n1,n2):
        n1,n2=sorted([n1,n2],key=lambda x:x.data)
        def dfs(cur=root):
            if not cur:
                return None
            if n1.data<=cur.data<=n2.data:
                return cur
            elif cur.data<n1.data:
                return dfs(cur.right)
            else:
                return dfs(cur.left)
        return dfs()
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)

arr=[5,4,6,3,"N","N",7,"N","N","N",8]
n1=7
n2=8
root=Node(0)
root=root.buildTree(arr)
print(root.LCA(root,n1,n2)) # type: ignore
print(root.otherApproach(root,root.right,root.right.right)) # type: ignore