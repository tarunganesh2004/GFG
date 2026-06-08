# Delete Nodes with Greater on Right

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head=None 

    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return 
        cur=self.head 
        while cur.next is not None:
            cur=cur.next
        cur.next=new_node

class Solution:
    def computeBruteForce(self,head):
        dummy=Node(0)
        dummy.next=head 

        prev=dummy 
        curr=head 

        while curr:

            temp=curr.next
            found_greater=False

            while temp:
                if temp.data>curr.data:
                    found_greater=True 
                    break 
                temp=temp.next 

            if found_greater:
                prev.next=curr.next 
            else:
                prev=curr 

            curr=curr.next 

        return dummy.next 

    # optimized
    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def compute(self, head):

        # Step 1: Reverse the list
        head = self.reverse(head)

        # Step 2: Remove nodes smaller than max seen
        max_so_far = head.data
        curr = head

        while curr and curr.next:
            if curr.next.data < max_so_far:
                curr.next = curr.next.next  # delete node
            else:
                curr = curr.next
                max_so_far = curr.data

        # Step 3: Reverse back
        return self.reverse(head)


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":

    arr = [12, 15, 10, 11, 5, 6, 2, 3]

    # For brute force
    ll1 = LinkedList()
    for x in arr:
        ll1.insert(x)

    # For optimized
    ll2 = LinkedList()
    for x in arr:
        ll2.insert(x)

    sol = Solution()

    print("Brute Force:")
    head1 = sol.computeBruteForce(ll1.head)
    print_list(head1)

    print("Optimized:")
    head2 = sol.compute(ll2.head)
    print_list(head2)
