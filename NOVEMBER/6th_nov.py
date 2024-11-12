# root to leaf paths sum

from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def buildTree(s):
    if not s or s[0] == "N":
        return None

    ip = list(map(str, s.split()))
    root = Node(int(ip[0]))
    q = deque()
    q.append(root)

    i = 1
    while i < len(ip):
        curNode = q.popleft()

        # Left child
        if ip[i] != "N":
            curNode.left = Node(int(ip[i]))
            q.append(curNode.left)
        i += 1

        # Right child
        if i < len(ip) and ip[i] != "N":
            curNode.right = Node(int(ip[i]))
            q.append(curNode.right)
        i += 1

    return root


class Solution:
    def treePathSum(self, root):
        # res = [0]
        return self.dfs(root, 0)
        # return res[0]

    def dfs(self, root, curSum):
        if not root:
            return 0

        # Update current path sum
        curSum = curSum * 10 + root.data

        # If leaf node, add current path sum to result
        if not root.left and not root.right:
            # res[0] += curSum
            # print(res)
            return curSum

        else:
            # Recur for left and right children
            return self.dfs(root.left, curSum)+self.dfs(root.right, curSum)


if __name__ == "__main__":
    s = "6 3 5 2 5 N 4 N N 7 4 N N N N N N"
    root = buildTree(s)
    print(Solution().treePathSum(root))
