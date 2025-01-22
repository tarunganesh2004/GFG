# Add Number Linked Lists

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(val)  # type: ignore

    def printll(self):
        values = []
        cur = self.head
        while cur:
            values.append(str(cur.val))
            cur = cur.next
        print(" -> ".join(values))

    def reverse(self, head):
        prev = None
        cur=head
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        return prev
    
    def trim_zeros(self, head):
        while head is not None and head.val == 0:
            head = head.next
        return head

    # def add_two_numbers(self, l1, l2):
        # if l1 is None:
        #     return l1
        # if l2 is None:
        #     return l2
        # l1=self.trim_zeros(l1)
        # l2=self.trim_zeros(l2)
        # l1=self.reverse(l1)
        # l2=self.reverse(l2)

        # head=l1
        # prev=None
        # carry=0
        # sum=0
        # while l1 is not None and l2 is not None:
        #     sum=l1.val+l2.val+carry
        #     carry=sum//10
        #     l1.val=sum%10
        #     prev=l1
        #     l1=l1.next
        #     l2=l2.next
        
        # if l2 is not None or l1 is not None:
        #     if l2 is not None:
        #         prev.next=l2 # type: ignore
        #     l1=prev.next # type: ignore
        #     while l1 is not None:
        #         sum=l1.val+carry
        #         carry=sum//10
        #         l1.val=sum%10
        #         prev=l1
        #         l1=l1.next
        # if carry>0:
        #     prev.next=Node(carry) # type: ignore
        # return self.reverse(head)

    def addTwoNumbers(self,l1,l2):
        l1=self.reverse(l1)
        l2=self.reverse(l2)
        carry=0
        temp=Node(0)
        cur=temp
        while l1 or l2 or carry:
            ve=(l1.val if l1 else 0)+(l2.val if l2 else 0)+carry
            cur.val=ve%10 # type: ignore
            if ve>=10:
                carry=1
            else:
                carry=0
            
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            cur.next=Node(0)
            cur=cur.next # type: ignore
        temp=self.reverse(temp)
        while temp.val==0: # type: ignore
            temp=temp.next # type: ignore
        return temp
        

ll1 = LinkedList()
num1 = [4, 5]
for i in num1:
    ll1.insert(i)
ll1.printll()

ll2 = LinkedList()
num2 = [3, 4, 5]
for i in num2:
    ll2.insert(i)
ll2.printll()

# Add the two numbers
ll3 = LinkedList()
ll3.head = ll3.addTwoNumbers(ll1.head, ll2.head)
ll3.printll()