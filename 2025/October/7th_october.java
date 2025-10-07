// Bottom View of Binary Tree 
import java.util.*;
class Node{
    int data;
    Node left,right;

    Node(int d){
        data=d;
        left=right=null;
    }
}

class BinaryTree {
    Node root;

    public static Node buildTree(int[] arr) {
        if (arr.length == 0 || arr[0] == -1) {
            return null;
        }
        Node root = new Node(arr[0]);
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < arr.length) {
            Node curr = q.poll();
            if (arr[i] != -1) {
                curr.left = new Node(arr[i]);
                q.add(curr.left);
            }
            i++;
            if (i >= arr.length)
                break;
            if (i < arr.length && arr[i] != -1) {
                curr.right = new Node(arr[i]);
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }
}

class Pair {
    Node node;
    int hd;

    Pair(Node n, int h) {
        node = n;
        hd = h;
    }
}

class Solution {
    public static ArrayList<Integer> bottomView(Node root) {
        ArrayList<Integer> ans = new ArrayList<>();
        if (root == null) return ans;

        Map<Integer, Integer> map = new TreeMap<>();
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(root, 0));

        while (!q.isEmpty()) {
            Pair p = q.poll();
            Node node = p.node;
            int hd = p.hd;

            map.put(hd, node.data);

            if (node.left != null) {
                q.add(new Pair(node.left, hd - 1));
            }
            if (node.right != null) {
                q.add(new Pair(node.right, hd + 1));
            }
        }

        for (int val : map.values()) {
            ans.add(val);
        }

        return ans;
    }
}

class Main{
    public static void main(String[] args) {
        int[] arr = {20,8,22,5,3,-1,25,-1,-1,10,14};
        // BinaryTree tree = new BinaryTree();
        Node root = BinaryTree.buildTree(arr);
        ArrayList<Integer> result = Solution.bottomView(root);
        System.out.println(result);
    }
}