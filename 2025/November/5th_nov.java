// Get Minimum Squares
import java.util.*;

class Solution {
    public int minSquares(int n) {
        if (isPerfectSquare(n)) return 1;

        for (int i = 1; i * i <= n; i++) {
            int j = n - i * i;
            if (isPerfectSquare(j)) return 2;
        }
        // check if n fits 4^a*(8b+7)
        while (n % 4 == 0) n /= 4;
        if (n % 8 == 7) return 4;
        
        return 3;
    }

    private boolean isPerfectSquare(int n) {
        int sqrt = (int)Math.sqrt(n);
        return sqrt * sqrt == n;
    }
}