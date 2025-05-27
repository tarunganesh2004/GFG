# Print leaf nodes from preorder traversal of BST

preorder=[5,2,10]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_leaf_nodes(preorder):
    if not preorder:
        return []
    
    root= Node(preorder[0])
    stack=[root]
    for value in preorder[1:]:
        node=Node(value)
        if value<stack[-1].data:
            stack[-1].left=node # type: ignore
        else:
            parent=None
            while stack and value>stack[-1].data:
                parent=stack.pop()
            parent.right=node # type: ignore
        
        stack.append(node)

    leaf_nodes = []
    def find_leaf_nodes(node):
        if not node:
            return
        if not node.left and not node.right:
            leaf_nodes.append(node.data)
        find_leaf_nodes(node.left)
        find_leaf_nodes(node.right)
    find_leaf_nodes(root)
    return leaf_nodes
    

print(print_leaf_nodes(preorder))