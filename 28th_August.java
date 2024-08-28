// https://www.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency-1587115621/1

import java.util.*;
class solution {
    public static void main(String[] args) {
        int[] arr = { 5, 5, 4, 6, 4 };
        System.out.println(sort(arr));
    }

    public static List<Integer> sort(int[] a) {
        int n = a.length;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(a[i], map.getOrDefault(a[i], 0) + 1);
        }
        List<Integer> list = new ArrayList<>(map.keySet());
        Collections.sort(list, (x, y) -> {
            if (map.get(x) == map.get(y)) {
                return x - y;
            }
            return map.get(y) - map.get(x);
        });
        List<Integer> ans = new ArrayList<>();
        for (int i : list) {
            int freq = map.get(i);
            while (freq-- > 0) {
                ans.add(i);
            }
        }
        return ans;
    }
}