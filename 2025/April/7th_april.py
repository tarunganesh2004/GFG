# Directed Graph Cycle

v=4
edges=[[0,1],[1,2],[2,3],[3,1]]

def isCyclic(v,edges):
    adj=[[] for _ in range(v)]
    for src,dest in edges:
        adj[src].append(dest)
    
    vis=[False]*v
    stack=[False]*v
    def dfs(node):
        vis[node]=True
        stack[node]=True
        for neighbour in adj[node]:
            if not vis[neighbour]:
                if dfs(neighbour):
                    return True
            elif stack[neighbour]:
                return True
        stack[node]=False
        return False
    
    for i in range(v):
        if not vis[i]:
            if dfs(i):
                return True
    
    return False

print(isCyclic(v,edges))