# # Serialize and deserialize a binary tree

# Serialization is to store a tree in an array so that it can be later restored and deserialization is reading tree back from the array. Complete the functions

# serialize() : stores the tree into an array a and returns the array.
# deSerialize() : deserializes the array to the tree and returns the root of the tree.
# Note: Multiple nodes can have the same data and the node values are always positive integers. Your code will be correct if the tree returned by deSerialize(serialize(input_tree)) is same as the input tree. Driver code will print the in-order traversal of the tree returned by deSerialize(serialize(input_tree)).


from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def buildTree(self, arr):
        if not arr or arr[0] == "N":
            return None
        q = []
        root = Node(arr[0])
        i = 1
        q.append(root)
        while i < len(arr) and q:
            node = q.pop(0)
            if i < len(arr) and arr[i] != "N":
                node.left = Node(arr[i])
                q.append(node.left)
            i += 1
            if i >= len(arr):
                break
            if i < len(arr) and arr[i] != "N":
                node.right = Node(arr[i])
                q.append(node.right)
            i += 1
        return root

    def serialize(self, root):
        if not root:
            return ["N"]
        return [root.data] + self.serialize(root.left) + self.serialize(root.right)

    def deSerialize(self, arr):
        self.index = 0  
        return self._deSerializeHelper(arr)

    def _deSerializeHelper(self, arr):
        if self.index >= len(arr) or arr[self.index] == "N":
            self.index += 1  # Skip over 'N' or invalid node
            return None
        node = Node(arr[self.index])
        self.index += 1
        node.left = self._deSerializeHelper(arr)
        node.right = self._deSerializeHelper(arr)
        return node

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def serializeIterative(self,root):
        if not root:
            return []
        q=deque([root])
        res=[]
        while q:
            node=q.popleft()
            res.append(node.data if node else 'N')
            if node:
                q.append(node.left)
                q.append(node.right)
        return res
    
    def deSerializeIterative(self,arr):
        return self.buildTree(arr)


# Testing the implementation
arr = [1, 2, 3]
root = Node(0)
root = root.buildTree(arr)

print("In-order traversal of the original tree:")
root.inorder(root) # type: ignore
print()

serialized_tree = root.serialize(root) # type: ignore
print("Serialized tree:", serialized_tree)

deserialized_tree = root.deSerialize(serialized_tree) # type: ignore # type: ignore
print("In-order traversal of the deserialized tree:")
root.inorder(deserialized_tree) # type: ignore


print(root.serializeIterative(root)) # type: ignore
print(root.deSerializeIterative([1,2,3])) # type: ignore