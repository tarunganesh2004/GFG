// Replace O's with X's

import java.util.*;

class Solution {
    public static void main(String[] args) {
        char[][] grid = {
                { 'X', 'X', 'X', 'X' },
                { 'X', 'O', 'X', 'X' },
                { 'X', 'O', 'O', 'X' },
                { 'X', 'O', 'X', 'X' },
                { 'X', 'X', 'O', 'O' }
        };

        char[][] res = fill(grid);
        System.out.println(Arrays.deepToString(res));
    }
    
    static int[][] dir = { { -1, 0 }, { 0, -1 }, { 1, 0 }, { 0, 1 } };
    
    public static char[][] fill(char[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int[][] vis = new int[n][m];

        for (int j = 0; j < m; j++) {
            // first row
            if (grid[0][j] == 'O' && vis[0][j] == 0) {
                dfs(0, j, grid, vis);
            }
            // last row
            if (grid[n - 1][j] == 'O' && vis[n - 1][j] == 0) {
                dfs(n - 1, j, grid, vis);
            }
        }

        for (int i = 0; i < n; i++) {
            // first column
            if (grid[i][0] == 'O' && vis[i][0] == 0) {
                dfs(i, 0, grid, vis);
            }
            // last column
            if (grid[i][m - 1] == 'O' && vis[i][m - 1] == 0) {
                dfs(i, m - 1, grid, vis);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (vis[i][j] == 0 && grid[i][j] == 'O') {
                    grid[i][j] = 'X';
                }
            }
        }
        return grid;
    }
    
    public static void dfs(int row, int col, char[][] grid, int[][] vis) {
        vis[row][col] = 1;
        int n = grid.length;
        int m = grid[0].length;

        for (int i = 0; i < 4; i++) {
            int nrow = row + dir[i][0];
            int ncol = col + dir[i][1];

            if (nrow >= 0 && nrow < n && ncol >= 0 && ncol < m
                    && vis[nrow][ncol] == 0 && grid[nrow][ncol] == 'O') {
                dfs(nrow, ncol, grid, vis);
            }
        }
    }

}