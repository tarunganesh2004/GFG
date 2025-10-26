// Minimum Steps to Halve Sum 

import java.util.*;

class Solution {
    public static void main(String[] args) {
        int[] arr = { 8, 6, 2 };
        System.out.println(minOperations(arr));
    }

    public static int minOperations(int[] arr) {
        PriorityQueue<Double> pq = new PriorityQueue<>(Collections.reverseOrder());
        double sum = 0;
        for(int num : arr){
            pq.add((double)num);
            sum += num;
        }
        double target = sum / 2;
        int operations = 0;
        while(!pq.isEmpty() && sum > target){
            double curr = pq.poll();
            sum -= curr;
            pq.add(curr / 2);
            operations++;
        }
        return operations;
    }
}