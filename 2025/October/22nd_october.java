// Nearly sorted
import java.util.*;

class Solution {
    public static void main(String[] args) {
        int[] arr = { 2, 3, 1, 4 };
        int k = 2;
        nearlySorted(arr, k);
        System.out.println(Arrays.toString(arr));
    }

    public static void nearlySorted(int[] arr, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        int idx = 0;
        for (int i = 0; i < Math.min(k + 1, arr.length); i++) {
            minHeap.offer(arr[i]);
        }
        for (int i = k + 1; i < arr.length; i++) {
            arr[idx++] = minHeap.poll();
            minHeap.offer(arr[i]);
        }
        while (!minHeap.isEmpty()) {
            arr[idx++] = minHeap.poll();
        }
    }

}