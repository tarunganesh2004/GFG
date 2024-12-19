// N meetings in one room
import java.util.*;
class nMeetings {
    public static int maxMeetings(int n, int[] start, int[] end) {
        int[][] a = new int[n][2];
        for (int i = 0; i < n; i++) {
            a[i][0] = start[i];
            a[i][1] = end[i];
        }
        Arrays.sort(a, (x, y) -> x[1] - y[1]);
        // int s = a[0][0];
        int c = 0;
        int e = a[0][1];
        for (int i = 1; i < n; i++) {
            if (a[i][0] <= e) {
                continue;
            } else {
                c++;
                e = a[i][1];

            }
        }
        return c + 1;
    }
}