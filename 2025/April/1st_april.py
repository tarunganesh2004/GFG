# DFS Of Graph

adj=[[2,3,1],[0],[0,4],[0],[2]]

def dfs(adj):
    v=len(adj)
    visited=[False]*v
    res=[]
    for i in range(v):
        if not visited[i]:
            dfs_util(i,adj,visited,res)
    return res
    
def dfs_util(i,adj,visited,res):
    res.append(i)
    visited[i]=True
    for nei in adj[i]:
        if not visited[nei]:
            dfs_util(nei,adj,visited,res)


print(dfs(adj))