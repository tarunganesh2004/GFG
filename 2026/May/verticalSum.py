from collections import deque
class Node:
    def __init__(self,val):
        self.data=val 
        self.left=None 
        self.right=None 

class BinaryTree:
    def buildTree(self,arr):
        if len(arr)==0 or arr[0]==-1:
            return None 
        root=Node(arr[0])
        q=deque()
        q.append(root)
        i=1
        while q and i<len(arr):
            cur=q.popleft()
            if arr[i]!=-1:
                cur.left=Node(arr[i])
                q.append(cur.left)
            
            i+=1
            if i>=len(arr):
                break 
            if arr[i]!=-1:
                cur.right=Node(arr[i])
                q.append(cur.right)
            i+=1
        return root 

class Solution:
    def verticalSum(self,root):
        mp={}
        def dfs(node,col):
            if not node:
                return 
            if col not in mp:
                mp[col]=0
            
            mp[col]+=node.data
            dfs(node.left,col-1)
            dfs(node.right,col+1)
        dfs(root,0)
        print(mp)

        ans=[]
        for col in sorted(mp):
            ans.append(mp[col])
        return ans

bt=BinaryTree()
arr = [1, 2, 3, 4, -1, 5, 6]
root = bt.buildTree(arr)
obj= Solution()
ans = obj.verticalSum(root)
print(ans)