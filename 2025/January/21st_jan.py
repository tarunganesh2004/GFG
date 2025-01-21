# Linked List Group Reverse
# Given the head a linked list, the task is to reverse every k node in the linked list. If the number of nodes is not a multiple of k then the left-out nodes in the end, should be considered as a group and must be reversed.

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

    def reverse_k_group(self,head,k):
        if not head or k==1:
            return head
        
        # function to reverse a segment of the linked list
        def reverse_segment(start,end):
            prev,cur=None,start
            while cur!=end:
                next_node=cur.next
                cur.next=prev
                prev=cur
                cur=next_node
            return prev
        
        dummy=Node(0) # dummy node before the head
        dummy.next=head
        prev_group_end=dummy
        while True:
            # identify the start and end of the group
            group_start=prev_group_end.next # type: ignore
            group_end=prev_group_end
            for _ in range(k):
                group_end=group_end.next # type: ignore # type: ignore
                if not group_end:
                    return dummy.next # return new head if fewer than k nodes are left
                
            next_group_start=group_end.next # type: ignore
            group_end.next=None # type: ignore # type: ignore # Temporarily break the chain

            # reverse the current group
            reversed_group_head=reverse_segment(group_start,None)

            # connect the reversed group to the previous and next parts
            prev_group_end.next=reversed_group_head # type: ignore # connect the previous group to the reversed group
            group_start.next=next_group_start # type: ignore
            prev_group_end=group_start

                

    def reverseKGroup(self,head,k):
        if head is None:
            return None
        cur=head
        prev=None
        next=None
        count=0
        while cur is not None and count<k:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
            count+=1
        if next is not None:
            head.next=self.reverseKGroup(next,k)
        return prev
    

arr=[1,2,2,4,5,6,7,8]
k=4
ll=LinkedList()
for i in arr:
    ll.insert(i)
ll.printll()
ll.head=ll.reverseKGroup(ll.head,k)
ll.printll()
ll.head=ll.reverse_k_group(ll.head,k)
ll.printll()