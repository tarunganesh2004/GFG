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
public class transform {
    public static void main(String[] args) {
        int[] arr = { 11, 2, 29, 1, 7, 15, 40, -1, -1, -1, -1, -1, 35, -1 };
        // BinaryTree tree = new BinaryTree();
        Node root = BinaryTree.buildTree(arr);
        System.out.println("Inorder before transformation:");
        inorder(root);
        transformTree(root);
        System.out.println("\nInorder after transformation:");
        inorder(root);

    }
    
    public static void inorder(Node root) {
        if (root == null)
            return;
        inorder(root.left);
        System.out.print(root.data + " ");
        inorder(root.right);
    }

    static int sum;

    public static void transformTree(Node root) {
        sum = 0;
        transformUtil(root);
    }
    public static void transformUtil(Node root) {
        if (root == null)
            return;
        transformUtil(root.right);
        int rootVal = root.data;
        root.data = sum;
        sum += rootVal;
        transformUtil(root.left);
    }
}
