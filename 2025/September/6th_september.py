# Find the Length of Loop

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
    

class LinkedList:
    def __init__(self):
        self.head=None 

    def insert(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return 
        current=self.head 
        while current.next is not None:
            current=current.next 
        current.next=newNode # type: ignore

    def printLL(self):
        current=self.head 
        while current is not None:
            print(current.data,end=" -> ")
            current=current.next 
        print("None")

class Solution:
    def detectLoop(self,head):
        if head is None:
            return 0 
        slow=head 
        fast=head 
        while fast is not None and fast.next is not None:
            slow=slow.next 
            fast=fast.next.next 
            if slow==fast:
                return self.countNodes(slow)
        return 0 

    def countNodes(self,slow):
        count=1
        current=slow 
        while current.next != slow:
            count+=1
            current=current.next 
        return count
    
ll=LinkedList()
arr=[1,2,3,4,5]
for i in arr:
    ll.insert(i)
ll.printLL()
