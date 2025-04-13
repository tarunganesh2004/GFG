# Clone an Undirected Graph

from sklearn import neighbors


n=4
adjList=[[1,2],[0,2],[0,1,3],[2]]



class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors 

class Solution():
    def cloneGraph(self,node):
        root=Node()
        seen={}
        def dfs(node=node,clone=root):
            nonlocal seen
            clone.val=node.val
            seen[clone.val]=clone
            for nei in node.neighbors:
                if nei.val in seen:
                    clone.neighbors.append(seen[nei.val])
                    continue
                clone.neighbors.append(Node())
                dfs(nei,clone.neighbors[-1])
        dfs(node,root)
        return root
    

s=Solution()

nodes=[Node(i) for i in range(len(adjList))]
for i,neighbors in enumerate(adjList):  # noqa: F402
    nodes[i].neighbors=[nodes[j] for j in neighbors]

cloned=s.cloneGraph(nodes[0])