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
class validateBST {
    
    public static boolean isBST(node root) {
        return validate(root, null, null);
    }

    public static boolean validate(node root, node min, node max) {
        if (root == null)
            return true;
        if ((min != null && root.data <= min.data) || (max != null && root.data >= max.data)) {
            return false;
        }
        return validate(root.left, min, root) && validate(root.right, root, max);
   }
    
}
