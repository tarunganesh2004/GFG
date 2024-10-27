class node:

    def __init__(self,data):
        self.data=data
        self.next=None

from collections import Counter 
class Solution:
    def count(self,head,key):
        l=[]
        while head:
            l.append(head.data)
            head=head.next

        c=Counter(l)
        for k,v in c.items():
            if key==k:
                return v
            break
        return 0
    
    def anotherWay(self,head,key):
        fast=head
        c=0

        while fast !=None and fast.next!=None:
            if fast.data==key:
                c+=1

            if fast.next.data==key:
                c+=1
            
            fast=fast.next.next

        return c+(1 if fast!=None and fast.data==key else 0)
