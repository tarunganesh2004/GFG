// Find K Smallest Sum Pairs from Two Arrays
import java.util.*;

class Solution {
    public static void main(String[] args) {
        int[] nums1 = { 1, 7, 11 };
        int[] nums2 = { 2, 4, 6 };
        int k = 3;
        List<List<Integer>> result = kSmallestPairs(nums1, nums2, k);
        for (List<Integer> pair : result) {
            System.out.println(pair);
        }
    }

    public static List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> res = new ArrayList<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> (a[0] + a[1]) - (b[0] + b[1]));

        for (int i = 0; i < Math.min(nums1.length, k); i++) {
            for (int j = 0; j < Math.min(nums2.length, k); j++) {
                pq.offer(new int[] { nums1[i], nums2[j] });
            }
        }

        while (k > 0 && !pq.isEmpty()) {
            int[] pair = pq.poll();
            res.add(Arrays.asList(pair[0], pair[1]));
            k--;
        }

        return res;
    }
}