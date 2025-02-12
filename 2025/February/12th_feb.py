# Kth Smallest Element in BST

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def buildTree(self,arr):
        if not arr or arr[0] == 'N':
            return None
        q=[]
        root=Node(arr[0])
        i=1
        q.append(root)
        while i<len(arr) and q:
            node=q.pop(0)
            if i<len(arr) and arr[i]!='N':
                node.left=Node(arr[i])
                q.append(node.left)
            i+=1
            if i>=len(arr):
                break
            if i<len(arr) and arr[i]!='N':
                node.right=Node(arr[i])
                q.append(node.right)
            i+=1
        return root
    
    def inorder(self, root, k, count, result):
        if root is None:
            return
        self.inorder(root.left, k, count, result)
        count[0] += 1
        if count[0] == k:
            result[0] = root.data
            return
        self.inorder(root.right, k, count, result)

    # Return the kth smallest element in the given BST
    def kthSmallest(self, root, k):
        count = [0]
        result = [-1]
        self.inorder(root, k, count, result)
        return result[0]

    # using Morris Traversal
    def kthSmallestOptimized(self,root,k):
        count = 0
        ksmall = None
        curr = root
        while curr:
            if curr.left is None:
                count += 1
                if count == k:
                    ksmall = curr.data
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                if pre.right is None:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    count += 1
                    if count == k:
                        ksmall = curr.data
                    curr = curr.right
        return ksmall

arr = [3,1,4,"N",2]
root = Node(None)
root = root.buildTree(arr)
print(root.kthSmallest(root,1)) # type: ignore # 1