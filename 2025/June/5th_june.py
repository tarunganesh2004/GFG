# Count the Paths 

# from functools import lru_cache


edges=[[0,1],[0,3],[2,0],[2,1],[1,3]]
v=4
src=2
dest=3

def count_paths(edges,v,src,dest):
    graph= [[] for _ in range(v)]
    for u, v in edges:
        graph[u].append(v) # Directed acyclic graph

    # print(graph)
    # @lru_cache(None)
    # def dfs(node):
    #     if node == dest:
    #         return 1
    #     count = 0
    #     for neighbor in graph[node]:
    #         count += dfs(neighbor)
    #     return count
    # return dfs(src)

    # the above code can be done using memoization
    dp=[-1]*v
    def dfs(node):
        if node == dest:
            return 1
        if dp[node] != -1:
            return dp[node]
        count = 0
        for neighbor in graph[node]:
            count += dfs(neighbor)
        dp[node] = count
        return count
    return dfs(src)

print(count_paths(edges, v, src, dest)) 