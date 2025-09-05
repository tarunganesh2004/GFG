# Sort a LinkedList of 0s,1s and 2s

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
    def sortList(self,head):
        if head is None:
            return None 
        c1,c2,c3 =0,0,0
        cur=head 
        while cur is not None:
            if cur.data==0:
                c1+=1
            elif cur.data==1:
                c2+=1
            else:
                c3+=1
            cur=cur.next
        
        cur=head 
        while c1 != 0:
            cur.data=0
            c1-=1
            cur=cur.next
        while c2 != 0:
            cur.data=1
            c2-=1
            cur=cur.next
        while c3 != 0:
            cur.data=2
            c3-=1
            cur=cur.next
        return head
    
arr=[1,2,0,1,2,0,1,0]
ll=LinkedList()
for i in arr:
    ll.insert(i)
ll.printLL()
s=Solution()
newHead=s.sortList(ll.head)
ll.head=newHead
ll.printLL()