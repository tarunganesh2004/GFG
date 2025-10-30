// Graph Diameter

import java.util.*;

class Solution {
    public static void main(String[] args) {
        int v = 6;
        // int e = 5;
        int[][] edges = { { 0, 1 }, { 0, 4 }, { 1, 3 }, { 1, 2 }, { 2, 5 } };
        System.out.println(diameter(v, edges));

    }
    static class BFSResult {
        int node;
        int dist;
        int[] distances;

        BFSResult(int node, int dist, int[] distances) {
            this.node = node;
            this.dist = dist;
            this.distances = distances;
        }
    }

    public static BFSResult bfsFarthest(int start, List<List<Integer>> adj) {
        int n = adj.size();
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        dist[start] = 0;
        while (!q.isEmpty()) {
            int node = q.poll();
            for (int neighbor : adj.get(node)) {
                if (dist[neighbor] == -1) {
                    dist[neighbor] = dist[node] + 1;
                    q.add(neighbor);
                }
            }
        }
        int farthestNode = start;
        int maxDist = 0;
        for (int i = 0; i < n; i++) {
            if (dist[i] > maxDist) {
                maxDist = dist[i];
                farthestNode = i;
            }
        }
        return new BFSResult(farthestNode, maxDist, dist);
    }
    public static int diameter(int v, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < v; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }
        // start from any node and find the farthest node from it
        BFSResult firstBFS = bfsFarthest(0, adj);
        // start from the farthest node found and find the farthest node from it
        BFSResult secondBFS = bfsFarthest(firstBFS.node, adj);
        return secondBFS.dist;
    }
}