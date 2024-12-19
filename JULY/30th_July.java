import java.util.ArrayList;

class rateInAMaze {
    public static void main(String[] args) {
        int[][] m = { { 1, 0, 0, 0 }, { 1, 1, 0, 1 }, { 1, 1, 0, 0 }, { 0, 1, 1, 1 } };
        ArrayList<String> res = findPath(m);
        for (String s : res) {
            System.out.println(s);
        }
    }
    public static ArrayList<String> findPath(int[][] m) {
        int n = m.length;
        ArrayList<String> res = new ArrayList<>();
        ArrayList<ArrayList<Boolean>> visited = new ArrayList<>(n);
        String path = "";
        for (int i = 0; i < n; i++) {
            ArrayList<Boolean> row = new ArrayList<>(n);
            for (int j = 0; j < n; j++) {
                row.add(false);
            }
            visited.add(row);
        }
        if (m[0][0] == 1) {
            solve(0, 0, m, res, n, visited, path);
        }
        return res;
    }

    public static void solve(int x, int y, int[][] m, ArrayList<String> l, int n, ArrayList<ArrayList<Boolean>> visited,
            String path) {
        if (x == n - 1 && y == n - 1) {
            l.add(path);
            return;
        }
        visited.get(x).set(y, true);
        if (isSafe(x + 1, y, n, m, visited)) {
            solve(x + 1, y, m, l, n, visited, path + "D");
        }
        if (isSafe(x, y - 1, n, m, visited)) {
            solve(x, y - 1, m, l, n, visited, path + "L");

        }
        if (isSafe(x, y + 1, n, m, visited)) {
            solve(x, y + 1, m, l, n, visited, path + "R");
        }
        if (isSafe(x - 1, y, n, m, visited)) {
            solve(x - 1, y, m, l, n, visited, path + "U");
        }
        visited.get(x).set(y, false);

    }
    
    public static boolean isSafe(int x, int y, int n,int[][] m, ArrayList<ArrayList<Boolean>> visited) {
        if ((x >= 0 && x < n) && (y >= 0 && y < n) && m[x][y] == 1 && (!visited.get(x).get(y))) {
            return true;
        }
        return false;
    }
}