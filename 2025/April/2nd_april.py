# BFS of a Graph

adj=[[2, 3, 1], [0], [0, 4], [0], [2]]

def bfs(adj):
    n=len(adj)
    visited=[False]*n
    res=[]
    for i in range(n):
        if not visited[i]:
            bfs_util(i,adj,visited,res)
    return res

def bfs_util(i,adj,visited,res):
    q=[i]
    visited[i]=True
    while q:
        node=q.pop(0)
        res.append(node)
        for nei in adj[node]:
            if not visited[nei]:
                q.append(nei)
                visited[nei]=True


print(bfs(adj))