// Shortest Cycle

import java.util.*;

class Solution {
    public static void main(String[] args) {
        int v = 7;
        // int e = 8;
        int[][] edges = { { 0, 5 }, { 0, 6 }, { 5, 1 }, { 6, 1 }, { 6, 2 }, { 2, 3 }, { 3, 4 }, { 1, 4 } };

        System.out.println(shortestCycle(v, edges));
    }

    public static int shortestCycle(int v, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < v; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        int shortestCycleLength = Integer.MAX_VALUE;

        for (int start = 0; start < v; start++) {
            int[] dist = new int[v];
            Arrays.fill(dist, -1);
            int[] parent = new int[v];
            Arrays.fill(parent, -1);
            Queue<Integer> q = new LinkedList<>();
            q.add(start);
            dist[start] = 0;

            while (!q.isEmpty()) {
                int node = q.poll();
                for (int neighbor : adj.get(node)) {
                    if (dist[neighbor] == -1) {
                        dist[neighbor] = dist[node] + 1;
                        parent[neighbor] = node;
                        q.add(neighbor);
                    } else if (parent[node] != neighbor) {
                        // A cycle is detected
                        int cycleLength = dist[node] + dist[neighbor] + 1;
                        shortestCycleLength = Math.min(shortestCycleLength, cycleLength);
                    }
                }
            }
        }

        return shortestCycleLength == Integer.MAX_VALUE ? -1 : shortestCycleLength;
    }
}