import java.util.*;

class node1 {
    int data;
    node1 next;

    node1(int data) {
        this.data = data;
        this.next = null;
    }
}
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
class BTfromLL{
    public static node convert(node1 head, node root) {
        if (head == null)
            return null;
        List<node> l = new ArrayList<>();
        node1 cur = head;
        while (cur != null) {
            l.add(new node(cur.data));
            cur = cur.next;
        }
        for (int i = 0; i < l.size(); i++) {
            if (2 * i + 1 < l.size()) {
                l.get(i).left = l.get(2 * i + 1);
            }
            if (2 * i + 2 < l.size()) {
                l.get(i).right = l.get(2 * i + 2);
            }
        }
        return l.get(0);
    }
}
