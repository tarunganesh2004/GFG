# Remove Loop in Linked List
# Given a linked list, remove the loop in it if present. The task is to complete the function removeTheLoop which takes only one argument the head of the linked list . The function removes the loop in the linked list if present.

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

    def loopHere(self,pos):
        if pos==0:
            return
        walk=self.head
        for i in range(1,pos):
            walk=walk.next # type: ignore
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
    
    def removeTheLoop(self,head):
        # 
        if head is None or head.next is None:
            return
        slow=head
        fast=head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                # if slow and fast meet , then loop is present
                slow=head

                # move the slow and fast pointers to find the node where the loop starts
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next

                # now slow is the first node of the loop
                # traverse the loop to find the node where loop ends and remove it
                while fast.next!=slow:
                    fast=fast.next
                fast.next=None
                return
        return
    
    # another approach
    def removeTheLoopAnother(self,head):
        # using hash table
        nodeSet=set()
        prev=None
        while head:
            if head in nodeSet:
                prev.next=None # type: ignore
                return
            nodeSet.add(head)
            prev=head
            head=head.next
        return



arr=[1,3,4]
pos=2
ll=LinkedList()
for i in arr:
    ll.insert(i)
ll.loopHere(pos)
print(ll.detect_loop())
ll.removeTheLoop(ll.head)
print(ll.detect_loop())