// Distance of nearest cell having 1 in a binary matrix

import java.util.*;

class Solution {
    public static void main(String[] args) {
        int[][] grid = { { 0, 1, 1, 0 }, { 1, 1, 0, 0 }, { 0, 0, 1, 1 } };
        int[][] result = updateMatrix(grid);
        for (int[] row : result) {
            System.out.println(Arrays.toString(row));
        }
    }

    public static int[][] updateMatrix(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        int[][] dist = new int[rows][cols];
        boolean[][] visited = new boolean[rows][cols];
        Queue<int[]> queue = new LinkedList<>();

        // Initialize the queue with all 1s positions
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (mat[r][c] == 1) {
                    queue.offer(new int[] { r, c });
                    visited[r][c] = true;
                }
            }
        }

        int[][] directions = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

        // BFS to find the nearest 1 for each cell
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0];
            int c = cell[1];

            for (int[] dir : directions) {
                int newRow = r + dir[0];
                int newCol = c + dir[1];

                if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols && !visited[newRow][newCol]) {
                    dist[newRow][newCol] = dist[r][c] + 1;
                    visited[newRow][newCol] = true;
                    queue.offer(new int[] { newRow, newCol });
                }
            }
        }

        return dist;
    }
}