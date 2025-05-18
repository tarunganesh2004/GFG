# Level Order in Spiral Form

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

    def buildTree(self,arr):
        if not arr or arr[0] == 'N':
            return None
        root=Node(arr[0])
        queue=[root]
        i=1
        while queue and i<len(arr):
            currNode=queue.pop(0)
            if arr[i]!='N':
                currNode.left=Node(arr[i])
                queue.append(currNode.left)
            i+=1
            if i>=len(arr):
                break
            if arr[i]!='N':
                currNode.right=Node(arr[i])
                queue.append(currNode.right)
            i+=1
        return root
    
class Solution:
    def findSpiral(self,root):
        if not root:
            return []
        level=0
        q=[]
        q.append(root)
        result=[]
        while q:
            level_size=len(q)
            level_nodes=[]
            
            for _ in range(level_size):
                node=q.pop(0)
                level_nodes.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level%2==0:
                # even level,right to left
                result.extend(level_nodes[::-1])
            else:
                # odd level,left to right
                result.extend(level_nodes)
            level+=1
        return result
        
    
arr=[10,20,30,40,60]

root=Node(0)
root=root.buildTree(arr)
s=Solution()
print(s.findSpiral(root))