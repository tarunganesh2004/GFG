# Sum of nodes on the longest path in a binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def buildTree(self, values):
        if not values:
            return None
        root = Node(values[0])
        queue = [root]
        i = 1
        while i < len(values):
            current = queue.pop(0)
            if values[i] is not None:
                current.left = Node(values[i])
                queue.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = Node(values[i])
                queue.append(current.right)
            i += 1
        return root
    
def longest_path_sum(root):
    dp={}
    def dfs(root,total,level):
        nonlocal dp 
        if not root:
            if level not in dp:
                dp[level] = total
            else:
                dp[level] = max(dp[level], total)
            return
        dfs(root.left, total + root.data, level + 1)
        dfs(root.right, total + root.data, level + 1)
    dfs(root, 0, 0)
    return dp[max(dp)]

arr=[4,2,5,7,1,2,3,None,None,6,None]
root = Node(0).buildTree(arr)
print(longest_path_sum(root))  # Output: 13 (4 + 2 + 1+6)