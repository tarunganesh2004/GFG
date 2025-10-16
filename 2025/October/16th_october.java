// Remove BST Keys Outside the Given Range
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

    public Node buildTree(int[] arr) {
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
    public void inorder(Node root) {
        if (root == null)
            return;
        inorder(root.left);
        System.out.print(root.data + " ");
        inorder(root.right);
    }
}

class Solution {
    public static Node removeOutsideRange(Node root, int l, int r) {
        if (root == null) {
            return null;
        }
        root.left = removeOutsideRange(root.left, l, r);
        root.right = removeOutsideRange(root.right, l, r);
        if (root.data < l) {
            return root.right;
        }
        if (root.data > r) {
            return root.left;
        }
        return root;
    }
    public static void main(String[] args) {
        int[] arr = { 6, -13, 14, -1, -8, 13, 15, -1, -1, 7 };
        int l = -10, r = 13;
        BinaryTree tree = new BinaryTree();
        Node root = tree.buildTree(arr);
        Node res = removeOutsideRange(root, l, r);
        tree.inorder(res);
    }
}