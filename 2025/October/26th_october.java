// Minimum Cost of Ropes

import java.util.*;

class Solution {
    public static void main(String[] args) {
        int[] arr = { 4, 3, 2, 6 };
        System.out.println(minCost(arr));
    }

    public static int minCost(int[] arr) {
        if (arr.length == 1) {
            return 0;
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int res = 0;
        for (int i : arr) {
            pq.offer(i);
        }

        while (pq.size() >= 2) {
            int first = pq.poll();
            int second = pq.poll();
            int sum = first + second;
            res += sum;
            pq.offer(sum);
        }
        return res;
    }
}