// K Closest points to Origin
import java.util.*;

class solution {
    public static void main(String[] args) {
        int[][] points = { { 1, 3 }, { -2, 2 }, { 5, 8 }, { 0, 1 } };
        int k = 2;
        System.out.println(Arrays.deepToString(kClosest(points, k)));
    }

    public static int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> maxHeap=new PriorityQueue<>(
            (a,b)-> (b[0]*b[0]+b[1]*b[1])- (a[0]*a[0]+a[1]*a[1])
        );
        for (int[] point : points) {
            maxHeap.add(point);
            if (maxHeap.size() > k) {
                maxHeap.poll();
            }
        }
        int[][] result = new int[k][2];
        for (int i = 0; i < k; i++) {
            result[i] = maxHeap.poll();
        }
        return result;
    }
}