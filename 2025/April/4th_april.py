# Undirected Graph Cycle 

v=4
e=4
edges=[[0,1],[0,2],[1,2],[2,3]]

# using bfs
def isCyclic(v,e,edges):
    def constructAdj(v,edges):
        adj=[[] for _ in range(v)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj
    
    def bfs(start,adj,visited):
        q=[start]
        visited[start]=True
        parent={start:-1}
        
        while q:
            node=q.pop(0)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor]=True
                    parent[neighbor]=node
                    q.append(neighbor)
                elif parent[node]!=neighbor:
                    return True
        return False
    
    adj=constructAdj(v,edges)
    visited=[False]*v
    for i in range(v):
        if not visited[i]:
            if bfs(i,adj,visited):
                return True
    return False

print(isCyclic(v,e,edges))