# Pair Sum in BST

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
    
    def isPairPresent(self, root, target):
        if root is None:
            return False
        s1 = []
        s2 = []
        done1 = False
        done2 = False
        val1 = 0
        val2 = 0
        curr1 = root
        curr2 = root
        while True:
            while not done1:
                if curr1:
                    s1.append(curr1)
                    curr1 = curr1.left
                else:
                    if not s1:
                        done1 = True
                    else:
                        curr1 = s1.pop()
                        val1 = curr1.data
                        curr1 = curr1.right
                        done1 = True
            while not done2:
                if curr2:
                    s2.append(curr2)
                    curr2 = curr2.right
                else:
                    if not s2:
                        done2 = True
                    else:
                        curr2 = s2.pop()
                        val2 = curr2.data
                        curr2 = curr2.left
                        done2 = True
            if val1 != val2 and val1 + val2 == target:
                return True
            elif val1 + val2 < target:
                done1 = False
            elif val1 + val2 > target:
                done2 = False
            if val1 >= val2:
                return False
        return False
    
    def isPairPresentOptimized(self, root, target):
        # using map to store the values
        s = set()
        return self.isPairPresentUtil(root, target, s)
    
    def isPairPresentUtil(self, root, target, s):
        if root is None:
            return False
        if self.isPairPresentUtil(root.left, target, s):
            return True
        if s and target - root.data in s:
            return True
        else:
            s.add(root.data)
        return self.isPairPresentUtil(root.right, target, s)
    
arr=[7,3,8,2,4,"N",9]
target=6
root = Node(0)
root = root.buildTree(arr)
print(root.isPairPresent(root, target)) # type: ignore
print(root.isPairPresentOptimized(root, target)) # type: ignore