# Linked List Group Reverse 

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
        else:
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=newNode # type: ignore

    def printLL(self):
        cur=self.head
        while cur is not None:
            print(cur.data,end=" -> ")
            cur=cur.next
        print("None")

class Solution:
    def reverseKGroup(self,head,k):
        if head is None:
            return None
        cur=head 
        prev=None 
        nextNode=None
        count=0

        while cur is not None and count<k:
            nextNode=cur.next
            cur.next=prev
            prev=cur
            cur=nextNode

            count+=1
        
        if nextNode is not None:
            head.next=self.reverseKGroup(nextNode,k)
        return prev
    
arr=[1,2,3,4,5]
ll=LinkedList()
k=2
for i in arr:
    ll.insert(i)
ll.printLL()
s=Solution()
newHead=s.reverseKGroup(ll.head,k)
ll.head=newHead
ll.printLL()