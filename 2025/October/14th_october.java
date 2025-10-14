// Sum of Nodes in BST Range

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

    public  Node buildTree(int[] arr) {
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

    private static int nodeSum(Node root, int l, int r) {
        if (root == null)
            return 0;
        int sum = 0;
        if (root.data >= l && root.data <= r) {
            sum += root.data;
        }
        if (root.data > l) {
            sum += nodeSum(root.left, l, r);
        }
        if (root.data < r) {
            sum += nodeSum(root.right, l, r);
        }
        return sum;
    }
    public static void main(String[] args) {
        int[] arr = { 22, 12, 30, 8, 20 };
        int l = 10;
        int r = 22;
        BinaryTree tree = new BinaryTree();
        Node root = tree.buildTree(arr);
        System.out.println(nodeSum(root, l, r));
    }
}