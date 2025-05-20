# Burning Tree

from collections import deque


class Node:
    def __init__(self,val):
        self.right=None
        self.data=val
        self.left=None

    def buildTree(self,arr):
        if not arr or arr[0]=="N":
            return None
        root=Node(arr[0])
        queue=[root]
        i=1
        while queue and i<len(arr):
            currNode=queue.pop(0)
            if arr[i]!="N":
                currNode.left=Node(arr[i])
                queue.append(currNode.left)
            i+=1
            if i>=len(arr):
                break
            if arr[i]!="N":
                currNode.right=Node(arr[i])
                queue.append(currNode.right)
            i+=1
        return root
    
class Solution:
    def minTime(self,root,target):
        if root is None:
            return -1
        q=deque([root])
        tar=None
        par={root:None}


        while q:
            cur=q.popleft()
            if cur.data==target:
                tar=cur

            # map the left and right child to the parent
            if cur.left:
                par[cur.left]=cur
                q.append(cur.left)
            if cur.right:
                par[cur.right]=cur
                q.append(cur.right)

        vis={}
        ans=-1
        q.append(tar)

        while q:
            size=len(q)
            for _ in range(size):
                cur=q.popleft()
                vis[cur]=True
                if cur.left and not vis.get(cur.left,False):
                    q.append(cur.left)
                if cur.right and not vis.get(cur.right,False):
                    q.append(cur.right)
                if par[cur] and not vis.get(par[cur],False):
                    q.append(par[cur])
            ans+=1
        return ans

    
root=[1,2,3,4,5,6,7]
target=2
n=Node(0)
root=n.buildTree(root)
s=Solution()
result=s.minTime(root,target)
print(result)