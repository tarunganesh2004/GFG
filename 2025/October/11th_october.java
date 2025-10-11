// Maximum Path Sum
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

class Solution {
    public static int maxPathSum(Node root) {
        if (root == null)
            return 0;
        int[] maxSum = new int[1];
        maxSum[0] = Integer.MIN_VALUE;
        findMaxPathSum(root, maxSum);
        return maxSum[0];
    }

    public static int findMaxPathSum(Node node, int[] maxSum) {
        if(node == null)
            return 0;
        int left = Math.max(0, findMaxPathSum(node.left, maxSum));
        int right = Math.max(0, findMaxPathSum(node.right, maxSum));
        maxSum[0] = Math.max(maxSum[0], left + right + node.data);

        return Math.max(left, right) + node.data;
        
    }


    public static void main(String[] args) {
        int[] arr={10,2,10,20,1,-1,-25,-1,-1,-1,-1,3,4};
        Node root = BinaryTree.buildTree(arr);
        System.out.println(maxPathSum(root));
    }
}