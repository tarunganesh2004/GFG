# Detect Loop in LinkedList
# You are given the head of a singly linked list. Your task is to determine if the linked list contains a loop. A loop exists in a linked list if the next pointer of the last node points to any other node in the list (including itself), rather than being null.

# Custom Input format:
# A head of a singly linked list and a pos (1-based index) which denotes the position of the node to which the last node points to. If pos = 0, it means the last node points to null, indicating there is no loop.

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
    
arr=[1,2,3,4]
ll=LinkedList()
pos=1
for i in arr:
    ll.insert(i)
ll.loopHere(pos)

print(ll.detect_loop()) # True