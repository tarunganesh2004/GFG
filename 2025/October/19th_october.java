// K Closest Values
import java.util.*;

class Node {
    int data;
    Node left, right;

    public Node(int data) {
        this.data = data;
        left = right = null;
    }
}

class BinaryTree {
    static Node root;

    public static Node buildTree(int[] arr) {
        if (arr[0] == -1 || arr.length == 0)
            return null;
        root = new Node(arr[0]);
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < arr.length) {
            Node cur = q.poll();
            if (arr[i] != -1) {
                cur.left = new Node(arr[i]);
                q.add(cur.left);
            }
            i++;
            if (i >= arr.length)
                break;
            if (arr[i] != -1) {
                cur.right = new Node(arr[i]);
                q.add(cur.right);
            }
            i++;
        }
        return root;
    }

}
class kclosest {
    public static void main(String[] args) {
        int[] arr = { 20, 8, 22, 4, 12, -1, -1, -1, -1, 10, 14 };
        int target = 17;
        int k = 3;
        // BinaryTree tree = new BinaryTree();
        Node root = BinaryTree.buildTree(arr);

        List<Integer> inorderList = new ArrayList<>();
        inorder(root, inorderList);
        int[] arr1 = new int[inorderList.size()];
        for (int i = 0; i < inorderList.size(); i++) {
            arr1[i] = inorderList.get(i);
        }

        System.out.println(Arrays.toString(findKClosestValues(arr1, target, k)));

        System.out.println(Arrays.toString(kClosestOptimized(root, target, k)));
    }
    
    public static void inorder(Node root, List<Integer> l) {
        if (root == null)
            return;
        inorder(root.left, l);
        l.add(root.data);
        inorder(root.right, l);
    }

    public static int[] findKClosestValues(int[] arr, int target, int k) {
        int[][] pairs = new int[arr.length][2];
        for (int i = 0; i < arr.length; i++) {
            pairs[i][0] = arr[i];
            pairs[i][1] = Math.abs(arr[i] - target);
        }
        System.out.println(Arrays.deepToString(pairs)); // now it stores pairs 

        // now sorting the pairs by the second element (the difference)
        Arrays.sort(pairs, (a, b) -> a[1] - b[1]);
        System.out.println(Arrays.deepToString(pairs)); // sorted pairs
        // return new int[] { 0, 0 };
        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = pairs[i][0];
        }
        return res;
    }

    // optimized way using two pointers

    public static int[] kClosestOptimized(Node root, int target, int k) {
        List<Integer> l = new ArrayList<>();
        inorder(root, l);
        int[] arr = l.stream().mapToInt(i -> i).toArray();

        int idx = findInsertIndex(arr, target);
        int left = idx - 1;
        int right = idx;
        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            if (left < 0) {
                res[i] = arr[right++];
            } else if (right >= arr.length) {
                res[i] = arr[left--];
            } else if (Math.abs(arr[left] - target) <= Math.abs(arr[right] - target)) {
                res[i] = arr[left--];
            } else {
                res[i] = arr[right++];
            }
        }
        return res;
    }
    
    private static int findInsertIndex(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
}