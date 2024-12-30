// https://www.geeksforgeeks.org/problems/sum-tree/1
class node {
    int data;
    node left;
    node right;

    node(int n) {
        data = n;
        left = null;
        right = null;
    }
}
class sumTree {
    boolean isSumTree(node root) {
        if (root == null)
            return true;
        if (root.left == null && root.right == null) {
            return true; // leaf node
        }
        boolean l = isSumTree(root.left);
        
        boolean r = isSumTree(root.right);

        int ls = findSum(root.left);
        int rs = findSum(root.right);
        if (l && r && (root.data == ls + rs)) {
            return true;
        } else {
            return false;
        }
    }
    
    int findSum(node root) {
        if (root == null)
            return 0;
        return root.data + findSum(root.left) + findSum(root.right);
    }
}