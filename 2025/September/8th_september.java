// merge sort for linked list 

class Node{
    int data;
    Node next;
    Node(int data){
        this.data = data;
        this.next = null;
    }
}
class LL{
    Node head;

    public void insert(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        } else {
            Node cur = head;
            while (cur.next != null) {
                cur = cur.next;
            }
            cur.next = newNode;
        }
    }

    public Node mergeSort(Node head) {
        if (head == null || head.next == null) {
            return head;
        }
        Node mid = getMid(head);
        Node left = mergeSort(head);
        Node right = mergeSort(mid);
        return merge(left, right);
    }

    private Node getMid(Node head) {
        Node slow = head;
        Node fast = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        Node mid = slow.next;
        slow.next = null;
        return mid;
    }

    private Node merge(Node left, Node right) {
        if (left == null) return right;
        if (right == null) return left;

        Node merged;
        if (left.data < right.data) {
            merged = left;
            merged.next = merge(left.next, right);
        } else {
            merged = right;
            merged.next = merge(left, right.next);
        }
        return merged;
    }
}

class mergesort {
    public static void main(String[] args) {
        int[] arr = { 40, 20, 60, 10, 50, 30 };
        LL ll = new LL();
        for (int num : arr) {
            ll.insert(num);
        }
        ll.head = ll.mergeSort(ll.head);
        Node cur = ll.head;
        while (cur != null) {
            System.out.print(cur.data + " ");
            cur = cur.next;
        }
    }
}