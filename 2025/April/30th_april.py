# Find the Length of the Loop 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None 
    
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node # type: ignore

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("NULL")

    def loop_here(self,pos):
        if pos==0:
            return 
        walk=self.head
        for i in range(1,pos):
            walk=walk.next # type: ignore

        tail=self.head
        while tail.next: # type: ignore
            tail=tail.next # type: ignore
        tail.next=walk # type: ignore

class Solution:
    def countNodesinLoop(self,head):
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next 
            slow=slow.next
            if slow==fast:
                break
        else:
            return 0
        count=1
        slow=slow.next
        while slow!=fast:
            count+=1
            slow=slow.next
        return count

arr=[1,2,3,4,5]
c=2 # loop is from last node to 2nd node 
ll=LinkedList()
for i in arr:
    ll.insert(i)
ll.printLL()
ll.loop_here(c)
# ll.printLL()
s=Solution()
print(s.countNodesinLoop(ll.head))