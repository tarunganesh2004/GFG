# Sort a Linked list of 0s, 1s and 2s

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

    
class Solution:
    def segregate(self,head):
        if head is None:
            return head
        
        zero_head = zero_tail = Node(0)
        one_head = one_tail = Node(0)
        two_head = two_tail = Node(0)
        
        current = head
        
        while current:
            if current.data == 0:
                zero_tail.next = current
                zero_tail = zero_tail.next
            elif current.data == 1:
                one_tail.next = current
                one_tail = one_tail.next
            else:
                two_tail.next = current
                two_tail = two_tail.next
            current = current.next
        
        # Connect the three lists
        zero_tail.next = one_head.next if one_head.next else two_head.next
        one_tail.next = two_head.next
        two_tail.next = None
        
        return zero_head.next
    

arr=[1,2,2,1,2,0,2,2]
ll=LinkedList()
for i in arr:
    ll.insert(i)
ll.printLL()
sol=Solution()
head=sol.segregate(ll.head)
ll.head=head
ll.printLL()