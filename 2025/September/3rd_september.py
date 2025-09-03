# Reverse a Double Linked List 

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
        self.prev=None 

class DLL:
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
            newNode.prev=cur # type: ignore

    def printDLL(self):
        cur=self.head
        while cur is not None:
            print(cur.data,end=" <=> ")
            cur=cur.next
        print("None")

class Solution:
    def reverseDLL(self,head):
        cur=head
        prev=None 

        while cur is not None:
            # swap next and prev for this node 
            nextNode=cur.next 
            cur.next,cur.prev=cur.prev,cur.next 

            # move prev and cur one step forward
            prev=cur
            cur=nextNode

        return prev

arr=[1,2,3,4,5]
dll=DLL()
for i in arr:
    dll.insert(i)
dll.printDLL()
s=Solution()
newHead=s.reverseDLL(dll.head)
dll.head=newHead
dll.printDLL()