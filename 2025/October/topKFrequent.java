// Top K Frequent In Array 
import java.util.*;
class topKFrequent{
    public static void main(String[] args) {
        int[] arr = { 3, 1, 4, 4, 5, 2, 6, 1 };
        int k = 2;
        System.out.println(topkfrequent(arr,k));
    }

    public static ArrayList<Integer> topkfrequent(int[] arr, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        // int n = arr.length;/
        for (int num : arr) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        List<Map.Entry<Integer, Integer>> l = new ArrayList<>(freqMap.entrySet());
        l.sort((a, b) -> {
            if (!a.getValue().equals(b.getValue())) {
                return b.getValue() - a.getValue();
            } else {
                return b.getKey() - a.getKey(); // descending, for ascending use a.getKey() - b.getKey()
            }
        });

        ArrayList<Integer> result = new ArrayList<>();
        for (int i = 0; i < k && i < l.size(); i++) {
            result.add(l.get(i).getKey());
        }
        return result;

    }

    // optimized 
    public static ArrayList<Integer> topkfrequentOptimized(int[] arr, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : arr) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Map.Entry<Integer, Integer>> minHeap = new PriorityQueue<>(
                (a, b) -> {
                    if (!a.getValue().equals(b.getValue())) {
                        return a.getValue() - b.getValue();
                    } else {
                        return b.getKey() - a.getKey(); // descending, for ascending use a.getKey() - b.getKey()
                    }
                }
        );

        for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
            minHeap.offer(entry);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }

        ArrayList<Integer> result = new ArrayList<>();
        while (!minHeap.isEmpty()) {
            result.add(minHeap.poll().getKey());
        }
        Collections.reverse(result); // To get the most frequent elements first
        return result;
    }
}