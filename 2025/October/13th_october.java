// Maximum Non Adjacent Nodes sum 

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
    public static int getMaxSum(Node root) {
        if (root == null) {
            return 0;
        }

        // include = include cur node and skip its children
        int include = root.data;
        if (root.left != null) {
            include += getMaxSum(root.left.left) + getMaxSum(root.left.right);
        }
        if (root.right != null) {
            include += getMaxSum(root.right.left) + getMaxSum(root.right.right);
        }

        // exclude= skip cur node and include its children
        int exclude = getMaxSum(root.left) + getMaxSum(root.right);

        return Math.max(include, exclude);
    }

    // optimized
    public static int getMaxSumOpt(Node root) {
        Map<Node, Integer> memo = new HashMap<>();
        return getMaxSumHelper(root, memo);
    }

    private static int getMaxSumHelper(Node node, Map<Node, Integer> memo) {
        if (node == null) {
            return 0;
        }

        // if already computed
        if (memo.containsKey(node)) {
            return memo.get(node);
        }

        int include = node.data;
        if (node.left != null) {
            include += getMaxSumHelper(node.left.left, memo) + getMaxSumHelper(node.left.right, memo);
        }
        if (node.right != null) {
            include += getMaxSumHelper(node.right.left, memo) + getMaxSumHelper(node.right.right, memo);
        }

        int exclude = getMaxSumHelper(node.left, memo) + getMaxSumHelper(node.right, memo);
        
        int result = Math.max(include, exclude);
        memo.put(node, result);
        return result;
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, -1, 5, 6 };
        BinaryTree tree = new BinaryTree();
        Node root = tree.buildTree(arr);
        System.out.println(getMaxSum(root));
    }
}