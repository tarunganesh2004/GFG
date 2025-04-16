# Floyd Warshall
INF=10**8
dist=[[0,4,INF,5,INF],
      [INF,0,1,INF,6],
      [2,INF,0,3,INF],
      [INF,INF,1,0,2],
      [1,INF,INF,4,0]
      ]

def floyd_warshall(dist):
    v=len(dist)
    for k in range(v):
        for i in range(v):
            for j in range(v):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    
        

floyd_warshall(dist)
print(dist)
# The time complexity of the Floyd-Warshall algorithm is O(V^3), where V is the number of vertices in the graph. This is because the algorithm uses three nested loops to iterate over all pairs of vertices and update the shortest path distances.