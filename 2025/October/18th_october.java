// Median of BST 

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
    public static int findMedian(Node root) {
        List<Integer> l = new ArrayList<>();
        inorder(root, l);
        int n = l.size();
        if (n % 2 == 0) {
            return l.get((n - 1) / 2);
        }
        return l.get(n / 2);
    }

    private static void inorder(Node root, List<Integer> l) {
        if (root == null)
            return;
        inorder(root.left, l);
        l.add(root.data);
        inorder(root.right, l);
    }
    

    public static void main(String[] args) {
        int[] arr = { 20, 8, 22, 4, 12, -1, -1, -1, -1, 10, 14 };
        Node root = BinaryTree.buildTree(arr);
        int median = findMedian(root);
        System.out.println("Median of BST is: " + median);
    }
}