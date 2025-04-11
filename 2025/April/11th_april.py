# Dijkstra Algorithm


def dijkstra(n, edges, src):
    import heapq

    # build adjacency list
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))  # For undirected graph

    # initialize distances
    dist = [float("inf")] * n
    dist[src] = 0
    visited = [False] * n
    pq = [(0, src)]  # (distance, vertex)
    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        for neighbor, weight in adj[u]:
            if not visited[neighbor] and d + weight < dist[neighbor]:
                dist[neighbor] = d + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
    return dist


v = 3
edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src = 2
print(dijkstra(v, edges, src))  # Output: [4, 3, 0]