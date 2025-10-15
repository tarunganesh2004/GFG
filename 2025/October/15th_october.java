// Kth Smallest Element in a BST

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
    public static int kthSmallest(Node root, int k) {
        int[] count = new int[1];
        for (int i = 0; i < count.length; i++) {
            count[i] = 0;
        }
        int[] res = new int[1];
        for (int i = 0; i < res.length; i++) {
            res[i] = -1;
        }
        kthSmallestUtil(root, k, count, res);
        return res[0];
    }

    private static void kthSmallestUtil(Node root, int k, int[] count,int[] res) {
        if (root == null) {
            return;
        }
        kthSmallestUtil(root.left, k, count, res);
        count[0]++;
        if (count[0] == k) {
            res[0] = root.data;
            return;
        }
        kthSmallestUtil(root.right, k, count, res);

    }
    public static void main(String[] args) {
        int[] arr = { 20, 8, 22, 4, 12, -1, -1, -1, -1, 10, 14 };
        int k = 3;
        BinaryTree tree = new BinaryTree();
        Node root = tree.buildTree(arr);

        System.out.println(kthSmallest(root, k));
    }
}