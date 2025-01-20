# Merge two sorted lists

class Node:
    def __init__(self,x):
        self.x=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,x):
        if self.head is None:
            self.head=Node(x)
        else:
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=Node(x) # type: ignore

    def printll(self):
        values=[]
        cur=self.head
        while cur:
            values.append(str(cur.x))
            cur=cur.next
        print(" -> ".join(values))
    
    def merge(self,l1,l2):
        dummy=Node(0) # dummy node to start the list
        cur=dummy # current node to traverse the list
        while l1 and l2:
            if l1.x<l2.x:
                cur.next=l1
                l1,cur=l1.next,l1 # move the pointer to next node and update the cur node to next node
            else:
                cur.next=l2
                l2,cur=l2.next,l2
        if l1 or l2:
            cur.next=l1 if l1 else l2
        return dummy.next


arr1=[5,10,15,40]
arr2=[2,3,20]
ll1=LinkedList()
ll2=LinkedList()
for i in arr1:
    ll1.insert(i)
for i in arr2:
    ll2.insert(i)

ll1.printll()
ll2.printll()
ll1.head=ll1.merge(ll1.head,ll2.head)
ll1.printll()