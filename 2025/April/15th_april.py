# Bellman Ford Algorithm

v=5
edges=[[1,3,2],[4,3,-1],[2,4,1],[1,2,1],[0,1,5]]
src=0

def bellman_ford(v, edges, src):
    INF=10**8
    distance=[INF] * v
    distance[src]=0

    for i in range(v-1):
        for u, v, w in edges:
            if distance[u] != INF and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in edges:
        if distance[u] != INF and distance[u] + w < distance[v]:
            return [-1]
    
    return distance

print(bellman_ford(v, edges, src))