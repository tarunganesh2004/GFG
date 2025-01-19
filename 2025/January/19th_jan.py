# Rotate a Linked List

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    
    def __str__(self):
        return str(self.val)
    
class LinkedList:

    def __init__(self):
        self.head=None

    def insert(self,x):
        if self.head is None:
            self.head=ListNode(x)
        else:
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=ListNode(x)  # type: ignore

    def printll(self):
        values=[]
        cur=self.head
        while cur:
            values.append(str(cur.val))
            cur=cur.next
        print(" -> ".join(values))

    def rotate(self,k):
        # Approach is to convert the linked list into a circular linked list
        # then traverse the list to the kth node 
        # the node at kth position will become new tail and k+1th node will become new head
        # update the head to k+1th node and kth node to Null
        if not self.head or not self.head.next or k==0:
            return self.head
        
        # convert to cll
        length=1
        tail=self.head
        while tail.next:
            tail=tail.next
            length+=1
        # make it circular
        tail.next=self.head # type: ignore

        # next find the new head and tail
        k%=length
        if k==0:
            tail.next=None # break the circular link
            return self.head
        
        cur=self.head
        for _ in range(k-1):
            cur=cur.next # type: ignore

        # update the head and tail
        new_head=cur.next # type: ignore
        cur.next=None # type: ignore # break the circular link

        return new_head

arr=[10,20,30,40,50]
k=4
ll=LinkedList()
for i in arr:
    ll.insert(i)
ll.printll()
ll.head=ll.rotate(k)
print("After rotating by",k)
ll.printll()