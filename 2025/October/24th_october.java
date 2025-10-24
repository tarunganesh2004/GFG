// Split Array Sunsequences

import java.util.*;

class Solution {
    public static void main(String[] args) {
        int[] arr = { 2, 2, 3, 3, 4, 5 };
        int k = 2;
        System.out.println(isPossible(arr, k));
    }

    public static boolean isPossible(int[] arr, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        Map<Integer, Integer> end = new HashMap<>();
        for (int num : arr) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        for (int num : arr) {
            if (count.get(num) == 0)
                continue;
            count.put(num, count.get(num) - 1);

            if (end.getOrDefault(num - 1, 0) > 0) {
                end.put(num - 1, end.get(num - 1) - 1);
                end.put(num, end.getOrDefault(num, 0) + 1);
            }
            else{
                boolean canFormNewSeq=true;
                for(int i=1;i<k;i++){
                    if(count.getOrDefault(num+i,0)<=0){
                        canFormNewSeq=false;
                        break;
                    }
                }
                if(!canFormNewSeq){
                    return false;
                }
                for(int i=1;i<k;i++){
                    count.put(num+i, count.get(num+i)-1);
                }
                end.put(num+k-1, end.getOrDefault(num+k-1, 0) + 1);
            }
        }
        return true;
    }
}