# Articulation Point - II

class Solution:
    def __init__(self):
        self.timer=1 # counts discovery times
        self.time=[] # to store discovery times of nodes
        self.low=[] # earliest visited node reachable from the subtree
        self.critical=[] # flag whether the node is articulation point or not

    def articulationPoints(self,v,edges):
        from collections import defaultdict
        adj=defaultdict(list)
        for src,dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        self.time=[0]*v
        self.low=[0]*v
        self.critical=[False]*v

        # start dfs
        for i in range(v):
            if self.low[i]==0:
                self.dfs(i,-1,adj)
        
        res=[i for i,is_critical in enumerate(self.critical) if is_critical]
        return res if res else [-1]
    
    def dfs(self,node,parent,adj):
        self.time[node]=self.low[node]=self.timer
        self.timer+=1
        children=0

        for neighbour in adj[node]:
            if neighbour==parent:
                continue
            
            if self.low[neighbour]==0:
                self.dfs(neighbour,node,adj)
                children+=1

                self.low[node]=min(self.low[node],self.low[neighbour])
                if parent!=-1 and self.low[neighbour]>=self.time[node]:
                    self.critical[node]=True
            else:
                self.low[node]=min(self.low[node],self.time[neighbour])

        if parent==-1 and children>1:
            self.critical[node]=True
        

sol=Solution()
v=5
edges=[(0,1),(0,2),(2,1),(0,3),(3,4)]
print(sol.articulationPoints(v,edges)) # [0, 3]

        