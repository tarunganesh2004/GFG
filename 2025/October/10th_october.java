// Zigzag Tree Traversal

import java.util.*;

class Node{
    int data;
    Node left,right;

    public Node(int data){
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

class Main {
    public static ArrayList<Integer> zigZagTraversal(Node root) {
        ArrayList<Integer> res = new ArrayList<>();
        ArrayList<Integer> temp = new ArrayList<>();
        if (root == null)
            return res;
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        // int n = 0;
        boolean leftToRight = true;
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                Node cur = q.poll();
                temp.add(cur.data);
                if (cur.left != null)
                    q.add(cur.left);

                if (cur.right != null)
                    q.add(cur.right);

            }
            if (!leftToRight) {
                Collections.reverse(temp);
            }
            res.addAll(temp);
            leftToRight = !leftToRight;

            temp.clear();

        }
        return res;
    }

    public static void main(String[] args) {
        int[] arr = { 7, 9, 7, 8, 8, 6, -1, 10, 9 };
        // BinaryTree tree = new BinaryTree();
        Node root = BinaryTree.buildTree(arr);
        ArrayList<Integer> ans = zigZagTraversal(root);
        System.out.println(ans);

    }
}
