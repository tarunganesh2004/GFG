# Bridge edge in a graph

# A bridge edge in a graph is an edge which, when removed, increases the number of connected components in the graph.

v=4
edges=[[0,1],[1,2],[2,3]]
def buildAdj(v,edges):
    adj=[[] for _ in range(v)]
    for src,dest in edges:
        adj[src].append(dest)
        adj[dest].append(src)
    return adj

adj=buildAdj(v,edges)
c=1
d=2

def isBridge(v,adj,c,d):
    if c in adj[d]:
        adj[d].remove(c)
    
    if d in adj[c]:
        adj[c].remove(d)

    else:
        return 0
    vis=[False]*v
    def dfs(node,vis):
        vis[node]=True
        for neighbour in adj[node]:
            if not vis[neighbour]:
                dfs(neighbour,vis)
    dfs(c,vis)
    if d in vis:
        return 0
    return 1

print(isBridge(v,adj,c,d))