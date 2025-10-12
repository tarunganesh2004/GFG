// Distribute Candies

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

class Test {
    private static int moves;

    public static int distCandy(Node root) {
        moves = 0;
        dfs(root);
        return moves;
    }
    
    private static int dfs(Node node) {
        if (node == null) return 0;
        int leftExcess = dfs(node.left);
        int rightExcess = dfs(node.right);
        moves += Math.abs(leftExcess) + Math.abs(rightExcess);

        // Return the excess candies at this node
        // left+ right+cur, we subtract 1 for the current node's need
        return node.data + leftExcess + rightExcess-1;
    }

    public static void main(String[] args) {
        int[] arr = { 5, 0, 0, -1, -1, 0, 0 };
        BinaryTree tree = new BinaryTree();
        Node root = tree.buildTree(arr);
        System.out.println(distCandy(root));
    }
}