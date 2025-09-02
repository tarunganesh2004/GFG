# Swap Kth Nodes from Ends



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
    
    def printll(self):
        cur=self.head 
        while cur is not None:
            print(cur.data,end="-->")
            cur=cur.next
        print("NULL")
    

class Solution:
    def swapKth(self,head,k):
        if head is None:
            return None
        n=0
        cur=head 
        while cur:
            n+=1
            cur=cur.next 
        if k>n:
            return head 
        
        if 2*k-1==n: # middle
            return head 
        
        first=head # kth node from beginning
        for _ in range(k-1):
            first=first.next

        second=head # kth node from end
        for _ in range(n-k):
            second=second.next

        first.data,second.data=second.data,first.data

        return head


arr=[1,2,3,4,5]
k=1

ll=LinkedList()
for i in arr:
    ll.insert(i)

ll.printll()

s=Solution()
head=s.swapKth(ll.head,k)
ll.printll()