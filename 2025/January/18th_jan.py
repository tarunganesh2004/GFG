# Reverse a LinkedList

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value) # type: ignore
    
    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev # type: ignore
            prev = current
            current = next
        self.head = prev
    
    def printll(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current) 
            if current.next is not None:
                result += " -> "
            current = current.next
        print(result)
    
ll = LinkedList()
arr=[1,2,3,4,5]
for i in arr:
    ll.insert(i)
ll.printll()
ll.reverse()
ll.printll()