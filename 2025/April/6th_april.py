# Topological Sort

v=4
e=3
edges=[[3,0],[1,0],[2,0]]

def topoSort(v,edges):
    adj=[[] for _ in range(v)]
    for u,v1 in edges:
        adj[u].append(v1)

    def dfs(node,vis,stack):
        vis[node]=True
        for neighbour in adj[node]:
            if not vis[neighbour]:
                dfs(neighbour,vis,stack)
        stack.append(node)
    
    vis=[False]*v
    stack=[]
    for i in range(v):
        if not vis[i]:
            dfs(i,vis,stack)
    
    return stack[::-1]

print(topoSort(v,edges))