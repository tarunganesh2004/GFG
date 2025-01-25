# Find the first node of loop in linked list

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert(self,val):
        if self.head is None:
            self.head=Node(val)
        else:
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=Node(val) # type: ignore

    def printll(self):
        values=[]
        cur=self.head
        while cur:
            values.append(str(cur.val))
            cur=cur.next
        print(" -> ".join(values))

    # adding loop at the given position
    def loopHere(self,pos):
        if pos==0:
            return
        walk=self.head
        for i in range(1,pos):
            walk=walk.next  # type: ignore
        last=walk
        while walk.next: # type: ignore
            walk=walk.next # type: ignore
        walk.next=last # type: ignore


    def detect_loop(self):
        slow=self.head
        fast=self.head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    
    def first_node_of_loop(self):
        slow=self.head
        fast=self.head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        slow=self.head
        while slow!=fast:
            slow=slow.next # type: ignore
            fast=fast.next # type: ignore
        return slow.val # type: ignore
    
    # another way is to use a set to store the nodes and check if the node is already present in the set
    def anotherWay(self,head):
        s=set()
        cur=head
        while cur:
            if cur in s:
                return cur.val
            s.add(cur)
            cur=cur.next
    
arr=[1,3,2,4,5]
ll=LinkedList()
pos=2
for i in arr:
    ll.insert(i)
ll.loopHere(pos)
print(ll.first_node_of_loop()) # 3