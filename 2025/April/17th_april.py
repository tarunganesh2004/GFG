# Minimum Weight Cycle

v=5
edges = [[0, 1, 2], [1, 2, 2], [1, 3, 1], [1, 4, 1], [0, 4, 3], [2, 3, 4]]

def findMinCycle(v, edges):
    from collections import defaultdict
    import heapq

    # create adjacency list
    graph = defaultdict(list)
    for a, b, w in edges:
        graph[a].append((b, w))

    INF = float("inf")
    min_cycle = INF

    # for each edge, remove it and run dijkstra
    for a, b, w in edges:
        # temporarily remove the edge a-b
        graph[a].remove((b, w))
        graph[b].remove((a, w))

        # run dijkstra from a
        dist = [INF] * v
        dist[a] = 0
        pq = [(0, a)]
        while pq:
            d, x = heapq.heappop(pq)
            if d > dist[x]:
                continue
            for y, wt in graph[x]:
                if dist[y] > d + wt:
                    dist[y] = d + wt
                    heapq.heappush(pq, (dist[y], y))

        if dist[b] != INF:
            min_cycle = min(min_cycle, dist[b] + w)

        # add the edge back
        graph[a].append((b, w))
        graph[b].append((a, w))

    return min_cycle if min_cycle != INF else -1


print(findMinCycle(v, edges))  