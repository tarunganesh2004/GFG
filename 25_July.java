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
class arrayToBST{
    public static void main(String[] args) {
        int[] a = { 1, 2, 3, 4 };
        node root = arraytoBst(a);
        System.out.println(root.data);
    }

    public static node arraytoBst(int[] nums) {
        return convert(nums, 0, nums.length - 1);
    }

    public static node convert(int[] nums, int low, int high) {
        if (low > high)
            return null;
        int mid = low + (high - low) / 2;
        node root = new node(nums[mid]);
        root.left = convert(nums, low, mid -1);
        root.right = convert(nums, mid +1, high);
        return root;
    }
}